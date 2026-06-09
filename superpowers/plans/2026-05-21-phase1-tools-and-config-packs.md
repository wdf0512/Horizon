# Horizon MCP Phase 1 — Tools & Config Packs Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship the four user-facing MCP tools (`hz_get_briefing`, `hz_search_history`, `hz_subscribe_topic`, plumbed `topic_keywords`) and three vertical config packs, all atop the existing `src/mcp/` pipeline, with no infrastructure changes.

**Architecture:** Each new tool is a thin `@mcp.tool()` wrapper around a new method on `HorizonPipelineService`. Pipeline reuse: `get_briefing` composes the existing `fetch → score → filter → enrich` flow with a topic-keyword steering signal. State is file-backed for now — Postgres swap is Phase 3. Topic awareness is opt-in: when `topic_keywords` is None, every code path behaves identically to today (backward compat is a hard requirement; existing tests must stay green).

**Tech Stack:** Python 3.11 · uv · FastMCP (`mcp>=1.0.0`, 1.26.0 installed) · pytest 8 · pydantic v2 · existing `ContentAnalyzer` in `src/ai/analyzer.py` · existing `RunStore` in `src/mcp/run_store.py`.

**Scope guard:** This plan covers Day 1–7 of the 14-day sprint. Days 8–14 (HTTP transport, Postgres, auth/quota, billing, landing page) are out of scope and live in separate plans (Phase 2–5). Do **not** add Fly.io, Postgres, Stripe, FastAPI, or middleware code here — even forward-compat hooks. The cache key shape (Task 2.1) is the one exception: it leaves `tenant_id` in place so Phase 4 wiring is mechanical.

**What this plan corrects from `docs/COMMERCIAL_SPEC.md`:**
- Scoring prompts live in `src/ai/prompts.py` (`CONTENT_ANALYSIS_SYSTEM/USER` constants) and the analyzer picks one based on `metadata.category` in `src/ai/analyzer.py:140-190`. The spec's reference to `src/ai/scoring.py` is wrong.
- Tests are flat under `tests/test_mcp_*.py` (see `tests/test_mcp_service_smoke.py`). Do **not** create `tests/mcp/` subdir.
- Subscription channel adapters (`feishu`, `slack`, `email`) do **not** exist; only `src/services/webhook.py` does. Day 5 here ships **storage only** — channel adapters are Phase 5 work.
- The existing `_run_tool` wrapper at `src/mcp/server.py:94` is mandatory for any new async tool (it records metrics + error shape). Don't bypass it.

---

## File Structure

**New files:**
- `src/mcp/cache.py` — pure LRU + TTL `BriefingCache` class (no I/O)
- `src/mcp/subscriptions_store.py` — file-backed `SubscriptionStore` CRUD (`data/subscriptions.json`)
- `src/mcp/models.py` — pydantic models for `Subscription` (kept tiny; one model only)
- `config_packs/SCHEMA.md` — config pack JSON schema documentation
- `config_packs/ai-developers.json` + `ai-developers.README.md`
- `config_packs/livestream-compliance.json` + `livestream-compliance.README.md`
- `config_packs/overseas-policy.json` + `overseas-policy.README.md`
- `tests/test_mcp_briefing.py`
- `tests/test_mcp_cache.py`
- `tests/test_mcp_search_history.py`
- `tests/test_mcp_topic_keywords.py`
- `tests/test_mcp_subscriptions.py`
- `tests/test_mcp_config_packs.py`

**Modified files:**
- `src/mcp/service.py` — adds `get_briefing`, `search_history`, `subscribe_topic`, `list_subscriptions`, `delete_subscription`; threads optional `topic_keywords` through `score_items`/`filter_items`/`run_pipeline`
- `src/mcp/server.py` — registers new tools, all wrapped with `_run_tool`
- `src/mcp/horizon_adapter.py` — adds `load_config_pack(name)` helper
- `src/ai/analyzer.py` — `analyze_batch` and `_analyze_item` accept optional `topic_keywords`; only the `category=""` (default) branch uses it
- `src/ai/prompts.py` — adds `TOPIC_RELEVANCE_ADDENDUM` constant + helper to splice into `CONTENT_ANALYSIS_USER`
- `src/mcp/README.md` — tool table refresh (Task 7.1 only)
- `.gitignore` — add `data/subscriptions.json`

**Untouched:** `Dockerfile`, `pyproject.toml`, `fly.toml` (doesn't exist), `src/mcp/run_store.py`, `src/orchestrator.py`, every other source file.

---

## Pre-flight Check (Task 0)

Run **before** Task 1.1. If any step fails, stop and resolve before proceeding.

- [ ] **Step 0.1: Confirm on `feat/commercial-sprint` branch**

```bash
git branch --show-current
```
Expected: `feat/commercial-sprint`

- [ ] **Step 0.2: Confirm working tree state**

```bash
git status --short
```
Expected: only the three untracked files (`docs/COMMERCIAL_SPEC.md`, `docs/IMPLEMENTATION_PLAN.md`, `scripts/to_xiaohongshu.py`) — nothing else modified.

- [ ] **Step 0.3: Sync deps + baseline test pass**

```bash
uv sync
uv run pytest -q
```
Expected: all existing tests pass. Note the green count; this is the floor every task must preserve.

- [ ] **Step 0.4: Sanity-check MCP server boots**

```bash
uv run python scripts/check_mcp.py
```
Expected: prints something like `13 tools registered`, no traceback.

---

## Task 1.1 — `_topic_to_keywords` Helper (Pure Function)

**Goal:** Convert a freeform topic string (`"LLM inference"`) into a normalized keyword list for prompt steering and cache keys. Pure function, easy to test.

**Files:**
- Modify: `src/mcp/service.py` (add module-level helper above `HorizonPipelineService`)
- Test: `tests/test_mcp_briefing.py` (new)

- [ ] **Step 1.1.1: Write the failing test**

Create `tests/test_mcp_briefing.py`:

```python
from __future__ import annotations

from src.mcp.service import _topic_to_keywords


def test_topic_to_keywords_splits_and_lowercases():
    assert _topic_to_keywords("LLM Inference") == ["llm", "inference"]


def test_topic_to_keywords_strips_stopwords():
    assert _topic_to_keywords("the future of AI in 2026") == ["future", "ai", "2026"]


def test_topic_to_keywords_dedupes_preserving_order():
    assert _topic_to_keywords("AI ai inference AI") == ["ai", "inference"]


def test_topic_to_keywords_handles_empty():
    assert _topic_to_keywords("") == []
    assert _topic_to_keywords("   ") == []
```

- [ ] **Step 1.1.2: Run the test, verify it fails**

```bash
uv run pytest tests/test_mcp_briefing.py -q
```
Expected: 4 failures, error mentions `ImportError: cannot import name '_topic_to_keywords'`.

- [ ] **Step 1.1.3: Add the helper to `src/mcp/service.py`**

Insert at the top of the file, after the existing `_default_runs_root` function (around `src/mcp/service.py:32`):

```python
_TOPIC_STOPWORDS = frozenset(
    {
        "a", "an", "the", "of", "and", "or", "in", "on", "at", "for",
        "to", "by", "with", "from", "is", "are", "was", "were",
    }
)


def _topic_to_keywords(topic: str) -> list[str]:
    """Normalize a freeform topic string into a deduped keyword list.

    Lowercases, splits on non-alphanumerics, drops stopwords, preserves order.
    """
    tokens: list[str] = []
    seen: set[str] = set()
    current: list[str] = []
    for ch in topic.lower():
        if ch.isalnum():
            current.append(ch)
        else:
            if current:
                tokens.append("".join(current))
                current = []
    if current:
        tokens.append("".join(current))

    out: list[str] = []
    for tok in tokens:
        if not tok or tok in _TOPIC_STOPWORDS:
            continue
        if tok in seen:
            continue
        seen.add(tok)
        out.append(tok)
    return out
```

- [ ] **Step 1.1.4: Run the test, verify it passes**

```bash
uv run pytest tests/test_mcp_briefing.py -q
```
Expected: 4 passed.

- [ ] **Step 1.1.5: Confirm full suite still green**

```bash
uv run pytest -q
```
Expected: no regressions.

- [ ] **Step 1.1.6: Commit**

```bash
git add src/mcp/service.py tests/test_mcp_briefing.py
git commit -m "feat(mcp): add _topic_to_keywords helper for briefing tool"
```

---

## Task 1.2 — `service.get_briefing` (No Cache, No Topic Plumbing Yet)

**Goal:** Implement the briefing method end-to-end using the existing pipeline. This first cut runs the full pipeline and post-filters items whose `ai_summary` or `title` mentions any of the topic keywords. Cache lands in Task 2.2; deeper topic plumbing lands in Task 4.5.

**Files:**
- Modify: `src/mcp/service.py` (add `get_briefing` method on `HorizonPipelineService`)
- Test: `tests/test_mcp_briefing.py` (append)

- [ ] **Step 1.2.1: Write the failing tests**

Append to `tests/test_mcp_briefing.py`:

```python
import asyncio
from pathlib import Path
from types import SimpleNamespace

from src.mcp.service import HorizonPipelineService


def _fake_run_pipeline_factory(items_payload: list[dict]):
    async def fake_run_pipeline(self, **kwargs):
        return {
            "run_id": "20260521-fake",
            "fetch": {"fetched": len(items_payload)},
            "score": {"scored": len(items_payload)},
            "filter": {"kept": len(items_payload)},
            "enrich": {"enriched": len(items_payload)},
            "summaries": [],
            "meta": {},
        }
    return fake_run_pipeline


def _fake_load_items(stage_items: list[dict]):
    def loader(self, run_id, stage, max_items=200):
        return {"items": stage_items, "count": len(stage_items)}
    return loader


def test_get_briefing_returns_top_n_items_sorted_by_score(tmp_path, monkeypatch):
    service = HorizonPipelineService(runs_root=tmp_path / "mcp-runs")

    enriched = [
        {"title": "LLM inference speedup", "url": "u1", "source_type": "rss",
         "ai_score": 9.1, "ai_summary": "vllm faster"},
        {"title": "Unrelated news", "url": "u2", "source_type": "rss",
         "ai_score": 8.0, "ai_summary": "weather"},
        {"title": "Anthropic releases", "url": "u3", "source_type": "rss",
         "ai_score": 8.7, "ai_summary": "claude llm update"},
    ]

    monkeypatch.setattr(HorizonPipelineService, "run_pipeline",
                        _fake_run_pipeline_factory(enriched))
    monkeypatch.setattr(HorizonPipelineService, "get_run_stage",
                        _fake_load_items(enriched))

    result = asyncio.run(service.get_briefing(
        topic="LLM inference",
        hours=24,
        count=5,
        language="zh",
        min_score=7.0,
    ))

    assert result["topic"] == "LLM inference"
    assert result["language"] == "zh"
    assert result["item_count"] == 2  # only the two that mention llm/inference
    titles = [it["title"] for it in result["items"]]
    assert titles == ["LLM inference speedup", "Anthropic releases"]
    assert result["items"][0]["rank"] == 1
    assert result["items"][1]["rank"] == 2
    assert result["cached"] is False


def test_get_briefing_respects_count(tmp_path, monkeypatch):
    service = HorizonPipelineService(runs_root=tmp_path / "mcp-runs")
    enriched = [
        {"title": f"AI item {i}", "url": f"u{i}", "source_type": "rss",
         "ai_score": 9.0 - i * 0.1, "ai_summary": f"ai update {i}"}
        for i in range(10)
    ]
    monkeypatch.setattr(HorizonPipelineService, "run_pipeline",
                        _fake_run_pipeline_factory(enriched))
    monkeypatch.setattr(HorizonPipelineService, "get_run_stage",
                        _fake_load_items(enriched))

    result = asyncio.run(service.get_briefing(topic="AI", count=3))
    assert result["item_count"] == 3


def test_get_briefing_rejects_bad_language(tmp_path):
    service = HorizonPipelineService(runs_root=tmp_path / "mcp-runs")
    from src.mcp.errors import HorizonMcpError
    import pytest
    with pytest.raises(HorizonMcpError) as exc:
        asyncio.run(service.get_briefing(topic="x", language="fr"))
    assert exc.value.code == "HZ_INVALID_INPUT"
```

- [ ] **Step 1.2.2: Run the tests, verify failures**

```bash
uv run pytest tests/test_mcp_briefing.py -q
```
Expected: 3 failures, errors mention `AttributeError: ... has no attribute 'get_briefing'`.

- [ ] **Step 1.2.3: Implement `get_briefing` on `HorizonPipelineService`**

In `src/mcp/service.py`, add this method **after** the existing `run_pipeline` method (around `src/mcp/service.py:527`):

```python
    async def get_briefing(
        self,
        topic: str,
        hours: int = 24,
        count: int = 5,
        language: str = "zh",
        min_score: float = 7.0,
        config_pack: str | None = None,  # wired in Task 6.5
        horizon_path: str | None = None,
        config_path: str | None = None,
    ) -> dict[str, Any]:
        """One-call curated briefing: run pipeline, return top-N topic-relevant items."""

        if language not in ("zh", "en"):
            raise HorizonMcpError(
                code="HZ_INVALID_INPUT",
                message=f"language must be 'zh' or 'en', got {language!r}.",
            )
        if hours <= 0 or count <= 0:
            raise HorizonMcpError(
                code="HZ_INVALID_INPUT",
                message="hours and count must be positive.",
            )

        keywords = _topic_to_keywords(topic)

        pipeline_result = await self.run_pipeline(
            hours=hours,
            languages=[language],
            threshold=min_score,
            horizon_path=horizon_path,
            config_path=config_path,
            enrich=True,
            topic_dedup=True,
        )
        run_id = pipeline_result["run_id"]

        stage_payload = self.get_run_stage(run_id=run_id, stage="enriched", max_items=200)
        items = stage_payload.get("items", [])

        if keywords:
            def matches(item: dict[str, Any]) -> bool:
                haystack = " ".join(
                    str(item.get(field, "")).lower()
                    for field in ("title", "ai_summary", "ai_reason")
                )
                return any(kw in haystack for kw in keywords)
            items = [it for it in items if matches(it)]

        items.sort(key=lambda it: float(it.get("ai_score") or 0), reverse=True)
        items = items[:count]

        ranked = [
            {
                "rank": i + 1,
                "title": it.get("title"),
                "url": it.get("url"),
                "source": it.get("source_type"),
                "score": it.get("ai_score"),
                "summary": it.get("ai_summary"),
                "context": it.get("ai_context"),
            }
            for i, it in enumerate(items)
        ]

        return {
            "topic": topic,
            "language": language,
            "time_window_hours": hours,
            "cached": False,
            "run_id": run_id,
            "item_count": len(ranked),
            "items": ranked,
        }
```

- [ ] **Step 1.2.4: Run the tests, verify they pass**

```bash
uv run pytest tests/test_mcp_briefing.py -q
```
Expected: 4 (Task 1.1) + 3 = 7 passed.

- [ ] **Step 1.2.5: Confirm full suite is green**

```bash
uv run pytest -q
```

- [ ] **Step 1.2.6: Commit**

```bash
git add src/mcp/service.py tests/test_mcp_briefing.py
git commit -m "feat(mcp): add service.get_briefing wrapping run_pipeline with topic filter"
```

---

## Task 1.3 — Register `hz_get_briefing` MCP Tool

**Goal:** Expose `get_briefing` as an `@mcp.tool()`. Wrap in `_run_tool` so metrics + error shape are consistent with existing tools.

**Files:**
- Modify: `src/mcp/server.py` (add tool after `hz_run_pipeline` at line ~288)
- Test: `tests/test_mcp_briefing.py` (append)

- [ ] **Step 1.3.1: Write the failing test**

Append to `tests/test_mcp_briefing.py`:

```python
def test_hz_get_briefing_tool_returns_ok_envelope(tmp_path, monkeypatch):
    from src.mcp import server
    enriched = [
        {"title": "LLM bench", "url": "u1", "source_type": "rss",
         "ai_score": 9.0, "ai_summary": "llm bench"},
    ]
    monkeypatch.setattr(HorizonPipelineService, "run_pipeline",
                        _fake_run_pipeline_factory(enriched))
    monkeypatch.setattr(HorizonPipelineService, "get_run_stage",
                        _fake_load_items(enriched))

    result = asyncio.run(server.hz_get_briefing(topic="LLM", count=3))
    assert result["ok"] is True
    assert result["tool"] == "hz_get_briefing"
    assert result["data"]["item_count"] == 1
    assert "duration_ms" in result["meta"]


def test_hz_get_briefing_tool_returns_error_envelope_on_bad_language(monkeypatch):
    from src.mcp import server
    result = asyncio.run(server.hz_get_briefing(topic="x", language="fr"))
    assert result["ok"] is False
    assert result["error"]["code"] == "HZ_INVALID_INPUT"
```

- [ ] **Step 1.3.2: Run the test, verify failure**

```bash
uv run pytest tests/test_mcp_briefing.py::test_hz_get_briefing_tool_returns_ok_envelope -q
```
Expected: `AttributeError: module 'src.mcp.server' has no attribute 'hz_get_briefing'`.

- [ ] **Step 1.3.3: Register the tool in `src/mcp/server.py`**

Insert after `hz_run_pipeline` (after line 288):

```python
@mcp.tool()
async def hz_get_briefing(
    topic: str,
    hours: int = 24,
    count: int = 5,
    language: str = "zh",
    min_score: float = 7.0,
    config_pack: str | None = None,
    horizon_path: str | None = None,
    config_path: str | None = None,
) -> dict[str, Any]:
    """Return a curated briefing of top-N items on a topic.

    Wraps the full pipeline (fetch → score → filter → enrich) and filters
    the enriched stage by topic keywords derived from `topic`. Cache layer
    is added in a follow-up task.
    """

    return await _run_tool(
        "hz_get_briefing",
        lambda: service.get_briefing(
            topic=topic,
            hours=hours,
            count=count,
            language=language,
            min_score=min_score,
            config_pack=config_pack,
            horizon_path=horizon_path,
            config_path=config_path,
        ),
    )
```

- [ ] **Step 1.3.4: Run the tests, verify they pass**

```bash
uv run pytest tests/test_mcp_briefing.py -q
```
Expected: 9 passed.

- [ ] **Step 1.3.5: Manual MCP server smoke**

```bash
uv run python scripts/check_mcp.py
```
Expected: `14 tools registered` (was 13).

- [ ] **Step 1.3.6: Commit**

```bash
git add src/mcp/server.py tests/test_mcp_briefing.py
git commit -m "feat(mcp): register hz_get_briefing tool"
```

**Day 1 Gate:** `hz_get_briefing(topic="LLM inference", hours=24, count=5)` returns a valid envelope with `ok=true` and a ranked items list. Full suite green.

---

## Task 2.1 — `BriefingCache` (Pure LRU + TTL)

**Goal:** A standalone in-memory cache keyed on the briefing parameters. Multi-tenant-safe key shape from day one (Phase 4 just supplies a real `tenant_id`; today every call uses `"default"`). Pure data structure — no I/O, easy to unit-test deterministically.

**Files:**
- Create: `src/mcp/cache.py`
- Test: `tests/test_mcp_cache.py` (new)

- [ ] **Step 2.1.1: Write the failing test**

Create `tests/test_mcp_cache.py`:

```python
from __future__ import annotations

import time

from src.mcp.cache import BriefingCache, CacheKey


def test_cache_hit_within_ttl():
    cache = BriefingCache(max_entries=8, default_ttl_seconds=60, now=lambda: 1_000)
    key = CacheKey(tenant_id="default", topic="llm", language="zh",
                   hours=24, min_score=7.0, config_pack=None)
    cache.set(key, {"foo": "bar"})
    cache.now = lambda: 1_030  # within TTL
    assert cache.get(key) == {"foo": "bar"}


def test_cache_miss_after_ttl():
    cache = BriefingCache(max_entries=8, default_ttl_seconds=60, now=lambda: 1_000)
    key = CacheKey(tenant_id="default", topic="llm", language="zh",
                   hours=24, min_score=7.0, config_pack=None)
    cache.set(key, {"foo": "bar"})
    cache.now = lambda: 1_061  # past TTL
    assert cache.get(key) is None


def test_cache_miss_on_different_key():
    cache = BriefingCache(max_entries=8, default_ttl_seconds=60, now=lambda: 1_000)
    a = CacheKey(tenant_id="default", topic="llm", language="zh",
                 hours=24, min_score=7.0, config_pack=None)
    b = CacheKey(tenant_id="default", topic="llm", language="en",  # different lang
                 hours=24, min_score=7.0, config_pack=None)
    cache.set(a, {"x": 1})
    assert cache.get(b) is None


def test_cache_evicts_lru_when_full():
    cache = BriefingCache(max_entries=2, default_ttl_seconds=60, now=lambda: 1_000)
    k = lambda topic: CacheKey(tenant_id="default", topic=topic, language="zh",
                               hours=24, min_score=7.0, config_pack=None)
    cache.set(k("a"), 1)
    cache.set(k("b"), 2)
    cache.get(k("a"))      # bump 'a' to most-recent
    cache.set(k("c"), 3)   # should evict 'b' (LRU)
    assert cache.get(k("a")) == 1
    assert cache.get(k("b")) is None
    assert cache.get(k("c")) == 3


def test_cache_returns_expiry_timestamp():
    cache = BriefingCache(max_entries=4, default_ttl_seconds=120, now=lambda: 5_000)
    key = CacheKey(tenant_id="default", topic="x", language="zh",
                   hours=1, min_score=7.0, config_pack=None)
    cache.set(key, {"k": "v"})
    entry = cache.get_entry(key)
    assert entry is not None
    assert entry.expires_at == 5_120


def test_cache_invalidate_removes_entry():
    cache = BriefingCache(max_entries=4, default_ttl_seconds=60, now=lambda: 1_000)
    key = CacheKey(tenant_id="default", topic="x", language="zh",
                   hours=24, min_score=7.0, config_pack=None)
    cache.set(key, {"k": "v"})
    cache.invalidate(key)
    assert cache.get(key) is None
```

- [ ] **Step 2.1.2: Run the test, verify failure**

```bash
uv run pytest tests/test_mcp_cache.py -q
```
Expected: collection error / `ModuleNotFoundError: src.mcp.cache`.

- [ ] **Step 2.1.3: Create `src/mcp/cache.py`**

```python
"""In-memory LRU+TTL cache for briefing responses.

Pure data structure. Multi-tenant-safe key shape so that Phase 4 only needs
to supply a real tenant_id without changing this file.
"""
from __future__ import annotations

import time
from collections import OrderedDict
from dataclasses import dataclass
from typing import Any, Callable


@dataclass(frozen=True)
class CacheKey:
    tenant_id: str
    topic: str
    language: str
    hours: int
    min_score: float
    config_pack: str | None


@dataclass(frozen=True)
class CacheEntry:
    value: Any
    expires_at: float  # absolute epoch seconds


class BriefingCache:
    """Bounded LRU cache with per-entry TTL."""

    def __init__(
        self,
        max_entries: int = 256,
        default_ttl_seconds: int = 3600,
        now: Callable[[], float] = time.time,
    ) -> None:
        self._max = max_entries
        self._ttl = default_ttl_seconds
        self.now = now
        self._store: OrderedDict[CacheKey, CacheEntry] = OrderedDict()

    def get(self, key: CacheKey) -> Any | None:
        entry = self.get_entry(key)
        return entry.value if entry is not None else None

    def get_entry(self, key: CacheKey) -> CacheEntry | None:
        entry = self._store.get(key)
        if entry is None:
            return None
        if entry.expires_at <= self.now():
            del self._store[key]
            return None
        self._store.move_to_end(key)
        return entry

    def set(self, key: CacheKey, value: Any, ttl_seconds: int | None = None) -> None:
        ttl = ttl_seconds if ttl_seconds is not None else self._ttl
        self._store[key] = CacheEntry(value=value, expires_at=self.now() + ttl)
        self._store.move_to_end(key)
        while len(self._store) > self._max:
            self._store.popitem(last=False)

    def invalidate(self, key: CacheKey) -> None:
        self._store.pop(key, None)

    def __len__(self) -> int:
        return len(self._store)
```

- [ ] **Step 2.1.4: Run the test, verify it passes**

```bash
uv run pytest tests/test_mcp_cache.py -q
```
Expected: 6 passed.

- [ ] **Step 2.1.5: Commit**

```bash
git add src/mcp/cache.py tests/test_mcp_cache.py
git commit -m "feat(mcp): add BriefingCache (LRU + TTL, multi-tenant key shape)"
```

---

## Task 2.2 — Wire Cache Into `get_briefing` + `force_refresh` / `cached` Fields

**Goal:** Service uses a singleton `BriefingCache`. Second identical call within TTL returns cached payload with `cached: true` and `cached_until` ISO timestamp. `force_refresh=True` bypasses lookup but still writes the fresh result.

**Files:**
- Modify: `src/mcp/service.py` (instantiate cache in `__init__`, wrap `get_briefing` body)
- Modify: `src/mcp/server.py` (forward `force_refresh` param)
- Test: `tests/test_mcp_cache.py` (append)

- [ ] **Step 2.2.1: Write the failing test**

Append to `tests/test_mcp_cache.py`:

```python
import asyncio
from src.mcp.service import HorizonPipelineService


def _fake_run_pipeline_factory(items_payload):
    async def fake_run_pipeline(self, **kwargs):
        return {"run_id": "20260521-cached", "fetch": {}, "score": {},
                "filter": {}, "enrich": {}, "summaries": [], "meta": {}}
    return fake_run_pipeline


def _fake_get_run_stage(items_payload):
    def loader(self, run_id, stage, max_items=200):
        return {"items": items_payload, "count": len(items_payload)}
    return loader


def test_get_briefing_second_call_returns_cached_true(tmp_path, monkeypatch):
    enriched = [{"title": "ai update", "url": "u1", "source_type": "rss",
                 "ai_score": 9.0, "ai_summary": "ai inference"}]
    monkeypatch.setattr(HorizonPipelineService, "run_pipeline",
                        _fake_run_pipeline_factory(enriched))
    monkeypatch.setattr(HorizonPipelineService, "get_run_stage",
                        _fake_get_run_stage(enriched))

    service = HorizonPipelineService(runs_root=tmp_path / "mcp-runs")
    fixed_now = [1_000.0]
    service.briefing_cache.now = lambda: fixed_now[0]

    first = asyncio.run(service.get_briefing(topic="AI", hours=24, language="zh"))
    assert first["cached"] is False

    fixed_now[0] = 1_030.0  # 30s later, well within TTL
    second = asyncio.run(service.get_briefing(topic="AI", hours=24, language="zh"))
    assert second["cached"] is True
    assert "cached_until" in second
    assert second["items"] == first["items"]


def test_force_refresh_bypasses_cache(tmp_path, monkeypatch):
    enriched = [{"title": "x", "url": "u1", "source_type": "rss",
                 "ai_score": 9.0, "ai_summary": "ai"}]
    pipeline_calls = {"n": 0}

    async def counting_run_pipeline(self, **kwargs):
        pipeline_calls["n"] += 1
        return {"run_id": f"run-{pipeline_calls['n']}", "fetch": {},
                "score": {}, "filter": {}, "enrich": {}, "summaries": [], "meta": {}}

    monkeypatch.setattr(HorizonPipelineService, "run_pipeline", counting_run_pipeline)
    monkeypatch.setattr(HorizonPipelineService, "get_run_stage",
                        _fake_get_run_stage(enriched))

    service = HorizonPipelineService(runs_root=tmp_path / "mcp-runs")
    asyncio.run(service.get_briefing(topic="AI"))
    asyncio.run(service.get_briefing(topic="AI", force_refresh=True))
    assert pipeline_calls["n"] == 2
```

- [ ] **Step 2.2.2: Run the test, verify failure**

```bash
uv run pytest tests/test_mcp_cache.py::test_get_briefing_second_call_returns_cached_true -q
```
Expected: `AttributeError: ... 'briefing_cache'` or similar.

- [ ] **Step 2.2.3: Add cache field + `force_refresh` to `get_briefing`**

In `src/mcp/service.py`, add to the imports block at top:

```python
from datetime import datetime, timedelta, timezone
from .cache import BriefingCache, CacheKey
```

In `HorizonPipelineService.__init__`, after the existing assignment of `self._run_store = None`, add:

```python
        self.briefing_cache = BriefingCache(max_entries=256, default_ttl_seconds=3600)
```

Then rewrite `get_briefing` to consult the cache. Replace the existing implementation body (keep the validation block) with this version. The diff is: (a) add `force_refresh: bool = False` param, (b) build cache key after validation, (c) check cache before running pipeline, (d) store after, (e) return cached payload with updated `cached` / `cached_until` flags on hit.

```python
    async def get_briefing(
        self,
        topic: str,
        hours: int = 24,
        count: int = 5,
        language: str = "zh",
        min_score: float = 7.0,
        force_refresh: bool = False,
        config_pack: str | None = None,
        horizon_path: str | None = None,
        config_path: str | None = None,
    ) -> dict[str, Any]:
        """One-call curated briefing: run pipeline, return top-N topic-relevant items.

        Uses an in-memory LRU+TTL cache. Subsequent identical calls within
        the TTL window return the cached payload with `cached=true`.
        """

        if language not in ("zh", "en"):
            raise HorizonMcpError(
                code="HZ_INVALID_INPUT",
                message=f"language must be 'zh' or 'en', got {language!r}.",
            )
        if hours <= 0 or count <= 0:
            raise HorizonMcpError(
                code="HZ_INVALID_INPUT",
                message="hours and count must be positive.",
            )

        cache_key = CacheKey(
            tenant_id="default",        # filled in Phase 4
            topic=topic.strip().lower(),
            language=language,
            hours=hours,
            min_score=min_score,
            config_pack=config_pack,
        )

        if not force_refresh:
            cached_entry = self.briefing_cache.get_entry(cache_key)
            if cached_entry is not None:
                payload = dict(cached_entry.value)
                payload["cached"] = True
                payload["cached_until"] = datetime.fromtimestamp(
                    cached_entry.expires_at, tz=timezone.utc
                ).isoformat()
                # Honor a smaller `count` than what was cached, but never grow it.
                payload["items"] = payload["items"][:count]
                payload["item_count"] = len(payload["items"])
                return payload

        keywords = _topic_to_keywords(topic)

        pipeline_result = await self.run_pipeline(
            hours=hours,
            languages=[language],
            threshold=min_score,
            horizon_path=horizon_path,
            config_path=config_path,
            enrich=True,
            topic_dedup=True,
        )
        run_id = pipeline_result["run_id"]

        stage_payload = self.get_run_stage(run_id=run_id, stage="enriched", max_items=200)
        items = stage_payload.get("items", [])

        if keywords:
            def matches(item: dict[str, Any]) -> bool:
                haystack = " ".join(
                    str(item.get(field, "")).lower()
                    for field in ("title", "ai_summary", "ai_reason")
                )
                return any(kw in haystack for kw in keywords)
            items = [it for it in items if matches(it)]

        items.sort(key=lambda it: float(it.get("ai_score") or 0), reverse=True)
        items = items[:count]

        ranked = [
            {
                "rank": i + 1,
                "title": it.get("title"),
                "url": it.get("url"),
                "source": it.get("source_type"),
                "score": it.get("ai_score"),
                "summary": it.get("ai_summary"),
                "context": it.get("ai_context"),
            }
            for i, it in enumerate(items)
        ]

        payload = {
            "topic": topic,
            "language": language,
            "time_window_hours": hours,
            "cached": False,
            "run_id": run_id,
            "item_count": len(ranked),
            "items": ranked,
        }

        self.briefing_cache.set(cache_key, payload)
        return payload
```

- [ ] **Step 2.2.4: Forward `force_refresh` in `hz_get_briefing` tool**

In `src/mcp/server.py`, update the `hz_get_briefing` tool signature and the lambda payload to include `force_refresh: bool = False`. The diff:

Old signature line (Task 1.3): `min_score: float = 7.0,` then `config_pack: ...` etc.
New signature inserts `force_refresh: bool = False,` between `min_score` and `config_pack`:

```python
@mcp.tool()
async def hz_get_briefing(
    topic: str,
    hours: int = 24,
    count: int = 5,
    language: str = "zh",
    min_score: float = 7.0,
    force_refresh: bool = False,
    config_pack: str | None = None,
    horizon_path: str | None = None,
    config_path: str | None = None,
) -> dict[str, Any]:
    """Return a curated briefing of top-N items on a topic."""

    return await _run_tool(
        "hz_get_briefing",
        lambda: service.get_briefing(
            topic=topic,
            hours=hours,
            count=count,
            language=language,
            min_score=min_score,
            force_refresh=force_refresh,
            config_pack=config_pack,
            horizon_path=horizon_path,
            config_path=config_path,
        ),
    )
```

- [ ] **Step 2.2.5: Run the tests, verify they pass**

```bash
uv run pytest tests/test_mcp_cache.py tests/test_mcp_briefing.py -q
```
Expected: all green (8 from briefing + cache tests).

- [ ] **Step 2.2.6: Confirm full suite still green**

```bash
uv run pytest -q
```

- [ ] **Step 2.2.7: Commit**

```bash
git add src/mcp/service.py src/mcp/server.py tests/test_mcp_cache.py
git commit -m "feat(mcp): cache hz_get_briefing responses (LRU + TTL, force_refresh)"
```

**Day 2 Gate:** Two identical calls within 1h → second has `cached=true` and `cached_until` set. `force_refresh=true` always re-runs the pipeline.

---

## Task 3.1 — `service.search_history` (File-Backed)

**Goal:** Keyword + date-range search over historical `enriched`-stage artifacts from `RunStore`. ILIKE-style substring match on `title`, `ai_summary`, `ai_reason`. Sort by `ai_score` desc, return top-K.

**Files:**
- Modify: `src/mcp/service.py` (add method)
- Test: `tests/test_mcp_search_history.py` (new)

- [ ] **Step 3.1.1: Write the failing tests**

Create `tests/test_mcp_search_history.py`:

```python
from __future__ import annotations

import asyncio
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path

from src.mcp.service import HorizonPipelineService


def _seed_run(runs_root: Path, run_id: str, days_ago: int, items: list[dict]) -> None:
    run_dir = runs_root / run_id
    run_dir.mkdir(parents=True, exist_ok=True)
    created = (datetime.now(timezone.utc) - timedelta(days=days_ago)).isoformat()
    (run_dir / "meta.json").write_text(json.dumps({
        "run_id": run_id,
        "created_at": created,
        "updated_at": created,
    }), encoding="utf-8")
    (run_dir / "enriched_items.json").write_text(json.dumps(items), encoding="utf-8")


def test_search_history_returns_matching_items(tmp_path):
    runs_root = tmp_path / "mcp-runs"
    _seed_run(runs_root, "run-1", days_ago=1, items=[
        {"title": "Claude 4.7 released", "ai_score": 9.5,
         "ai_summary": "anthropic ships", "ai_reason": "major release",
         "url": "u1", "source_type": "rss"},
        {"title": "weather forecast", "ai_score": 8.0,
         "ai_summary": "rain", "ai_reason": "n/a",
         "url": "u2", "source_type": "rss"},
    ])
    _seed_run(runs_root, "run-2", days_ago=3, items=[
        {"title": "Anthropic API update", "ai_score": 8.7,
         "ai_summary": "claude pricing", "ai_reason": "policy",
         "url": "u3", "source_type": "rss"},
    ])

    service = HorizonPipelineService(runs_root=runs_root)
    result = asyncio.run(service.search_history(
        query="claude", days=7, top_k=5, min_score=7.0,
    ))

    assert result["count"] == 2
    titles = [it["title"] for it in result["items"]]
    assert titles == ["Claude 4.7 released", "Anthropic API update"]


def test_search_history_respects_date_window(tmp_path):
    runs_root = tmp_path / "mcp-runs"
    _seed_run(runs_root, "old", days_ago=30, items=[
        {"title": "Claude old", "ai_score": 9.0,
         "ai_summary": "x", "ai_reason": "y", "url": "u1", "source_type": "rss"},
    ])
    _seed_run(runs_root, "new", days_ago=1, items=[
        {"title": "Claude new", "ai_score": 9.0,
         "ai_summary": "x", "ai_reason": "y", "url": "u2", "source_type": "rss"},
    ])
    service = HorizonPipelineService(runs_root=runs_root)
    result = asyncio.run(service.search_history(query="claude", days=7, top_k=5))
    titles = [it["title"] for it in result["items"]]
    assert titles == ["Claude new"]


def test_search_history_filters_below_threshold(tmp_path):
    runs_root = tmp_path / "mcp-runs"
    _seed_run(runs_root, "r", days_ago=1, items=[
        {"title": "Claude A", "ai_score": 6.0,
         "ai_summary": "x", "ai_reason": "y", "url": "u1", "source_type": "rss"},
        {"title": "Claude B", "ai_score": 8.5,
         "ai_summary": "x", "ai_reason": "y", "url": "u2", "source_type": "rss"},
    ])
    service = HorizonPipelineService(runs_root=runs_root)
    result = asyncio.run(service.search_history(query="claude", days=7, min_score=7.0))
    titles = [it["title"] for it in result["items"]]
    assert titles == ["Claude B"]


def test_search_history_returns_empty_on_no_matches(tmp_path):
    runs_root = tmp_path / "mcp-runs"
    _seed_run(runs_root, "r", days_ago=1, items=[
        {"title": "weather", "ai_score": 9.0,
         "ai_summary": "rain", "ai_reason": "y", "url": "u1", "source_type": "rss"},
    ])
    service = HorizonPipelineService(runs_root=runs_root)
    result = asyncio.run(service.search_history(query="claude", days=7))
    assert result["count"] == 0
    assert result["items"] == []
```

- [ ] **Step 3.1.2: Run the tests, verify failure**

```bash
uv run pytest tests/test_mcp_search_history.py -q
```
Expected: `AttributeError: ... has no attribute 'search_history'`.

- [ ] **Step 3.1.3: Implement `search_history` in `src/mcp/service.py`**

Add this method after `get_briefing`:

```python
    async def search_history(
        self,
        query: str,
        days: int = 30,
        top_k: int = 10,
        min_score: float = 7.0,
    ) -> dict[str, Any]:
        """Keyword + date-range search over enriched artifacts."""

        if days <= 0 or top_k <= 0:
            raise HorizonMcpError(
                code="HZ_INVALID_INPUT",
                message="days and top_k must be positive.",
            )
        q = query.strip().lower()
        if not q:
            raise HorizonMcpError(
                code="HZ_INVALID_INPUT",
                message="query must be non-empty.",
            )

        cutoff = datetime.now(timezone.utc) - timedelta(days=days)
        candidates: list[dict[str, Any]] = []

        for entry in self.run_store.list_runs(limit=500):
            created_raw = entry.get("created_at")
            if not created_raw:
                continue
            try:
                created = datetime.fromisoformat(created_raw)
            except ValueError:
                continue
            if created < cutoff:
                continue
            if not self.run_store.has_stage(entry["run_id"], "enriched"):
                continue
            try:
                stage_items = self.run_store.load_items(entry["run_id"], "enriched")
            except FileNotFoundError:
                continue
            for item in stage_items:
                score = float(item.get("ai_score") or 0)
                if score < min_score:
                    continue
                haystack = " ".join(
                    str(item.get(field, "")).lower()
                    for field in ("title", "ai_summary", "ai_reason")
                )
                if q in haystack:
                    candidates.append({
                        "run_id": entry["run_id"],
                        "created_at": created_raw,
                        "title": item.get("title"),
                        "url": item.get("url"),
                        "source": item.get("source_type"),
                        "score": score,
                        "summary": item.get("ai_summary"),
                    })

        candidates.sort(key=lambda it: it["score"], reverse=True)
        items = candidates[:top_k]
        return {
            "query": query,
            "days": days,
            "min_score": min_score,
            "count": len(items),
            "items": items,
        }
```

Verify the test fixture is compatible: `RunStore.load_items` returns a `list[dict]` (verify in `src/mcp/run_store.py`); if it instead returns a dict with `"items"` key, adjust the loop above. **Verify before continuing:**

```bash
grep -n "def load_items" src/mcp/run_store.py
```
If the function returns `dict`, change `for item in stage_items:` to `for item in stage_items.get("items", []):`.

- [ ] **Step 3.1.4: Run the tests, verify they pass**

```bash
uv run pytest tests/test_mcp_search_history.py -q
```
Expected: 4 passed.

- [ ] **Step 3.1.5: Commit**

```bash
git add src/mcp/service.py tests/test_mcp_search_history.py
git commit -m "feat(mcp): add service.search_history with date-window keyword match"
```

---

## Task 3.2 — Register `hz_search_history` MCP Tool

**Files:**
- Modify: `src/mcp/server.py`
- Test: `tests/test_mcp_search_history.py` (append)

- [ ] **Step 3.2.1: Write the failing test**

Append to `tests/test_mcp_search_history.py`:

```python
def test_hz_search_history_tool_envelope(tmp_path, monkeypatch):
    from src.mcp import server
    monkeypatch.setattr(server.service, "search_history",
                        lambda **kw: _stub_result())
    async def _stub(): return {"count": 0, "items": [], "query": "x", "days": 7, "min_score": 7.0}
    async def _stub_result(): return await _stub()
    result = asyncio.run(server.hz_search_history(query="x", days=7))
    assert result["ok"] is True
    assert result["tool"] == "hz_search_history"
```

Simpler version — replace the test body with this cleaner monkeypatch:

```python
def test_hz_search_history_tool_envelope(tmp_path, monkeypatch):
    from src.mcp import server

    async def fake_search(**kwargs):
        return {"count": 0, "items": [], "query": kwargs["query"],
                "days": kwargs["days"], "min_score": kwargs["min_score"]}

    monkeypatch.setattr(server.service, "search_history", fake_search)

    result = asyncio.run(server.hz_search_history(query="claude", days=7))
    assert result["ok"] is True
    assert result["tool"] == "hz_search_history"
    assert result["data"]["query"] == "claude"
```

- [ ] **Step 3.2.2: Run the test, verify failure**

```bash
uv run pytest tests/test_mcp_search_history.py::test_hz_search_history_tool_envelope -q
```
Expected: `AttributeError: module 'src.mcp.server' has no attribute 'hz_search_history'`.

- [ ] **Step 3.2.3: Register the tool**

In `src/mcp/server.py`, insert after `hz_get_briefing`:

```python
@mcp.tool()
async def hz_search_history(
    query: str,
    days: int = 30,
    top_k: int = 10,
    min_score: float = 7.0,
) -> dict[str, Any]:
    """Keyword + date-range search over historical enriched items."""

    return await _run_tool(
        "hz_search_history",
        lambda: service.search_history(
            query=query,
            days=days,
            top_k=top_k,
            min_score=min_score,
        ),
    )
```

- [ ] **Step 3.2.4: Run the tests, verify they pass**

```bash
uv run pytest tests/test_mcp_search_history.py -q
```

- [ ] **Step 3.2.5: Commit**

```bash
git add src/mcp/server.py tests/test_mcp_search_history.py
git commit -m "feat(mcp): register hz_search_history tool"
```

**Day 3 Gate:** With ≥3 days of seeded runs, `hz_search_history(query="claude", days=7)` returns relevant items sorted by score.

---

## Task 4.1 — Plumb `topic_keywords` Through `ContentAnalyzer`

**Goal:** `analyze_batch(items, topic_keywords=None)` accepts an optional keyword list and threads it to `_analyze_item`. When `topic_keywords` is None or empty, behavior is **byte-identical** to today (prove this with a test that asserts the prompt sent to the AI client is unchanged).

**Files:**
- Modify: `src/ai/analyzer.py`
- Test: `tests/test_mcp_topic_keywords.py` (new)

- [ ] **Step 4.1.1: Write the failing test**

Create `tests/test_mcp_topic_keywords.py`:

```python
from __future__ import annotations

import asyncio
from datetime import datetime, timezone
from typing import Any

from src.ai.analyzer import ContentAnalyzer
from src.models import ContentItem, SourceType


class _CapturingAIClient:
    """Records every (system, user) prompt pair sent."""

    def __init__(self):
        self.calls: list[tuple[str, str]] = []
        self.config = type("Cfg", (), {"throttle_sec": 0.0})()

    async def complete(self, system: str, user: str) -> str:
        self.calls.append((system, user))
        return '{"score": 8.0, "reason": "stub", "summary": "stub", "tags": []}'


def _mk_item(item_id: str) -> ContentItem:
    return ContentItem(
        id=item_id,
        source_type=SourceType.RSS,
        title=f"Title {item_id}",
        url=f"https://example.com/{item_id}",
        content="some content",
        author="auth",
        published_at=datetime.now(timezone.utc),
    )


def test_analyze_batch_without_topic_keywords_does_not_change_prompt():
    client = _CapturingAIClient()
    analyzer = ContentAnalyzer(client)
    asyncio.run(analyzer.analyze_batch([_mk_item("a")]))

    assert len(client.calls) == 1
    system, user = client.calls[0]
    assert "Topic relevance" not in user
    assert "topic_keywords" not in user.lower()


def test_analyze_batch_with_topic_keywords_injects_addendum():
    client = _CapturingAIClient()
    analyzer = ContentAnalyzer(client)
    asyncio.run(analyzer.analyze_batch(
        [_mk_item("a")], topic_keywords=["llm", "inference"],
    ))

    assert len(client.calls) == 1
    _, user = client.calls[0]
    assert "Topic relevance" in user
    assert "llm" in user.lower()
    assert "inference" in user.lower()


def test_analyze_batch_empty_topic_keywords_treated_as_none():
    client = _CapturingAIClient()
    analyzer = ContentAnalyzer(client)
    asyncio.run(analyzer.analyze_batch(
        [_mk_item("a")], topic_keywords=[],
    ))
    _, user = client.calls[0]
    assert "Topic relevance" not in user
```

- [ ] **Step 4.1.2: Run the test, verify failure**

```bash
uv run pytest tests/test_mcp_topic_keywords.py -q
```
Expected: `TypeError: analyze_batch() got an unexpected keyword argument 'topic_keywords'`.

- [ ] **Step 4.1.3: Add the constant + helper in `src/ai/prompts.py`**

Append to the bottom of `src/ai/prompts.py`:

```python
TOPIC_RELEVANCE_ADDENDUM = """

Topic relevance (additional dimension):
The user is specifically tracking these topic keywords: {topic_keywords_str}
- If the content is directly relevant to the listed topics, weight it more heavily.
- If the content is only tangentially related, score it conservatively.
- If the content is unrelated to the listed topics, score below 5 regardless of intrinsic quality.
"""


def render_topic_addendum(topic_keywords: list[str] | None) -> str:
    """Return the topic-relevance block, or empty string if no keywords supplied."""
    if not topic_keywords:
        return ""
    return TOPIC_RELEVANCE_ADDENDUM.format(
        topic_keywords_str=", ".join(topic_keywords)
    )
```

- [ ] **Step 4.1.4: Thread `topic_keywords` through `ContentAnalyzer`**

In `src/ai/analyzer.py`:

1. Add import at top with the other prompts imports:
   ```python
   from .prompts import render_topic_addendum
   ```
2. Change `analyze_batch` signature (line ~44):
   ```python
   async def analyze_batch(
       self,
       items: List[ContentItem],
       topic_keywords: list[str] | None = None,
   ) -> List[ContentItem]:
   ```
3. Change the call to `self._analyze_item(item)` inside the loop (line ~59) to:
   ```python
   await self._analyze_item(item, topic_keywords=topic_keywords)
   ```
4. Change `_analyze_item` signature (line ~77):
   ```python
   async def _analyze_item(
       self,
       item: ContentItem,
       topic_keywords: list[str] | None = None,
   ) -> None:
   ```
5. In `_analyze_item`, locate the `else:` branch (around line 180) that builds `user_prompt = CONTENT_ANALYSIS_USER.format(...)`. After the `user_prompt = CONTENT_ANALYSIS_USER.format(...)` assignment, append:
   ```python
           user_prompt = user_prompt + render_topic_addendum(topic_keywords)
   ```

This deliberately limits the topic addendum to the default `CONTENT_ANALYSIS_USER` path — the compliance/dependency-risk/telegram-zh/ecosystem-signal branches are not changed, because those prompts have their own scoring rubrics that shouldn't be diluted.

- [ ] **Step 4.1.5: Run the tests, verify they pass**

```bash
uv run pytest tests/test_mcp_topic_keywords.py tests/test_analyzer.py -q
```
Expected: new tests pass; existing analyzer tests still pass.

- [ ] **Step 4.1.6: Full suite check**

```bash
uv run pytest -q
```

- [ ] **Step 4.1.7: Commit**

```bash
git add src/ai/analyzer.py src/ai/prompts.py tests/test_mcp_topic_keywords.py
git commit -m "feat(ai): plumb optional topic_keywords into ContentAnalyzer (backward-compatible)"
```

---

## Task 4.2 — Plumb `topic_keywords` Through Service Pipeline Methods

**Goal:** Add `topic_keywords: list[str] | None = None` as the final parameter of `service.score_items`, `service.run_pipeline`, and the `hz_run_pipeline` tool. Existing callers that don't pass it see unchanged behavior.

**Files:**
- Modify: `src/mcp/service.py`
- Modify: `src/mcp/server.py`
- Test: `tests/test_mcp_topic_keywords.py` (append)

- [ ] **Step 4.2.1: Write the failing test**

Append to `tests/test_mcp_topic_keywords.py`:

```python
from src.mcp.service import HorizonPipelineService
from src.mcp.errors import HorizonMcpError


def test_score_items_forwards_topic_keywords_to_analyzer(tmp_path, monkeypatch):
    """When topic_keywords is passed, the analyzer receives it."""

    captured = {"topic_keywords": "<not-called>"}

    class FakeAnalyzer:
        def __init__(self, client): pass
        async def analyze_batch(self, items, topic_keywords=None):
            captured["topic_keywords"] = topic_keywords
            return items

    config_path = tmp_path / "config.json"
    config_path.write_text("{}")

    fake_runtime = type("R", (), {
        "create_ai_client": lambda self, ai: object(),
        "ContentAnalyzer": FakeAnalyzer,
    })()
    fake_config = type("C", (), {"filtering": type("F", (), {"ai_score_threshold": 7.0})()})()

    service = HorizonPipelineService(runs_root=tmp_path / "mcp-runs")

    from types import SimpleNamespace
    monkeypatch.setattr(service, "_load_stage_items",
                        lambda **kw: ([SimpleNamespace(ai_score=9.0)],
                                      SimpleNamespace(runtime=fake_runtime, config=fake_config,
                                                      horizon_path=tmp_path, config_path=config_path)))
    monkeypatch.setattr("src.mcp.service.items_to_dicts", lambda items: [])
    monkeypatch.setattr(service.run_store, "save_items", lambda *a, **kw: None)
    monkeypatch.setattr(service.run_store, "update_meta", lambda *a, **kw: {})
    monkeypatch.setattr(service.run_store, "run_dir", lambda run_id: tmp_path)

    asyncio.run(service.score_items(
        run_id="r1", topic_keywords=["llm", "inference"],
    ))
    assert captured["topic_keywords"] == ["llm", "inference"]


def test_score_items_without_topic_keywords_passes_none(tmp_path, monkeypatch):
    captured = {"topic_keywords": "<not-called>"}

    class FakeAnalyzer:
        def __init__(self, client): pass
        async def analyze_batch(self, items, topic_keywords=None):
            captured["topic_keywords"] = topic_keywords
            return items

    config_path = tmp_path / "config.json"
    config_path.write_text("{}")

    fake_runtime = type("R", (), {
        "create_ai_client": lambda self, ai: object(),
        "ContentAnalyzer": FakeAnalyzer,
    })()
    fake_config = type("C", (), {"filtering": type("F", (), {"ai_score_threshold": 7.0})()})()

    service = HorizonPipelineService(runs_root=tmp_path / "mcp-runs")
    from types import SimpleNamespace
    monkeypatch.setattr(service, "_load_stage_items",
                        lambda **kw: ([SimpleNamespace(ai_score=9.0)],
                                      SimpleNamespace(runtime=fake_runtime, config=fake_config,
                                                      horizon_path=tmp_path, config_path=config_path)))
    monkeypatch.setattr("src.mcp.service.items_to_dicts", lambda items: [])
    monkeypatch.setattr(service.run_store, "save_items", lambda *a, **kw: None)
    monkeypatch.setattr(service.run_store, "update_meta", lambda *a, **kw: {})
    monkeypatch.setattr(service.run_store, "run_dir", lambda run_id: tmp_path)

    asyncio.run(service.score_items(run_id="r1"))
    assert captured["topic_keywords"] is None
```

- [ ] **Step 4.2.2: Run the tests, verify failure**

```bash
uv run pytest tests/test_mcp_topic_keywords.py::test_score_items_forwards_topic_keywords_to_analyzer -q
```
Expected: `TypeError: score_items() got an unexpected keyword argument 'topic_keywords'`.

- [ ] **Step 4.2.3: Add `topic_keywords` to `score_items`**

In `src/mcp/service.py`, edit `score_items` signature (line ~265):

```python
    async def score_items(
        self,
        run_id: str,
        source_stage: str = "raw",
        topic_keywords: list[str] | None = None,
        horizon_path: str | None = None,
        config_path: str | None = None,
    ) -> dict[str, Any]:
```

Change the analyzer call (line ~284):

```python
        scored_items = await analyzer.analyze_batch(items, topic_keywords=topic_keywords)
```

- [ ] **Step 4.2.4: Add `topic_keywords` to `run_pipeline`**

Edit `run_pipeline` signature (line ~455):

```python
    async def run_pipeline(
        self,
        hours: int = 24,
        languages: list[str] | None = None,
        threshold: float | None = None,
        horizon_path: str | None = None,
        config_path: str | None = None,
        sources: list[str] | None = None,
        enrich: bool = True,
        topic_dedup: bool = True,
        topic_keywords: list[str] | None = None,
        save_to_horizon_data: bool = False,
    ) -> dict[str, Any]:
```

Pass it down to `score_items` (line ~475):

```python
        score_result = await self.score_items(
            run_id=run_id,
            topic_keywords=topic_keywords,
            horizon_path=horizon_path,
            config_path=config_path,
        )
```

- [ ] **Step 4.2.5: Add `topic_keywords` to `hz_run_pipeline` tool**

In `src/mcp/server.py`, edit `hz_run_pipeline` signature (line ~262) — add `topic_keywords: list[str] | None = None` before `save_to_horizon_data`, and pass it through to `service.run_pipeline`:

```python
@mcp.tool()
async def hz_run_pipeline(
    hours: int = 24,
    languages: list[str] | None = None,
    threshold: float | None = None,
    horizon_path: str | None = None,
    config_path: str | None = None,
    sources: list[str] | None = None,
    enrich: bool = True,
    topic_dedup: bool = True,
    topic_keywords: list[str] | None = None,
    save_to_horizon_data: bool = False,
) -> dict[str, Any]:
    """Run fetch -> score -> filter -> enrich -> summarize in one call."""

    return await _run_tool(
        "hz_run_pipeline",
        lambda: service.run_pipeline(
            hours=hours,
            languages=languages,
            threshold=threshold,
            horizon_path=horizon_path,
            config_path=config_path,
            sources=sources,
            enrich=enrich,
            topic_dedup=topic_dedup,
            topic_keywords=topic_keywords,
            save_to_horizon_data=save_to_horizon_data,
        ),
    )
```

Same for `hz_score_items` (line ~174):

```python
@mcp.tool()
async def hz_score_items(
    run_id: str,
    source_stage: str = "raw",
    topic_keywords: list[str] | None = None,
    horizon_path: str | None = None,
    config_path: str | None = None,
) -> dict[str, Any]:
    """Score a stage into the scored stage."""

    return await _run_tool(
        "hz_score_items",
        lambda: service.score_items(
            run_id=run_id,
            source_stage=source_stage,
            topic_keywords=topic_keywords,
            horizon_path=horizon_path,
            config_path=config_path,
        ),
    )
```

- [ ] **Step 4.2.6: Run the tests, verify they pass**

```bash
uv run pytest tests/test_mcp_topic_keywords.py tests/test_mcp_service_smoke.py -q
```
Expected: green.

- [ ] **Step 4.2.7: Refactor `get_briefing` to use the topic_keywords path**

In `src/mcp/service.py` `get_briefing`, change the `run_pipeline` call to pass `topic_keywords` derived from the topic:

```python
        keywords = _topic_to_keywords(topic)

        pipeline_result = await self.run_pipeline(
            hours=hours,
            languages=[language],
            threshold=min_score,
            horizon_path=horizon_path,
            config_path=config_path,
            enrich=True,
            topic_dedup=True,
            topic_keywords=keywords or None,
        )
```

Keep the post-hoc `matches()` filter as a belt-and-braces — the prompt steering increases recall but doesn't guarantee 100% topic-on-topic items.

- [ ] **Step 4.2.8: Re-run briefing tests + full suite**

```bash
uv run pytest -q
```

- [ ] **Step 4.2.9: Commit**

```bash
git add src/mcp/service.py src/mcp/server.py tests/test_mcp_topic_keywords.py
git commit -m "feat(mcp): thread topic_keywords through score_items, run_pipeline, get_briefing"
```

**Day 4 Gate:** Backward compat — all existing tests pass without modification. New code path — `topic_keywords=["llm","inference"]` reaches the analyzer and modifies the prompt.

---

## Task 5.1 — `Subscription` Model + File-Backed Store

**Goal:** Pydantic model + JSON-file CRUD store at `data/subscriptions.json`. No scheduler execution this sprint — just persistence.

**Files:**
- Create: `src/mcp/models.py`
- Create: `src/mcp/subscriptions_store.py`
- Modify: `.gitignore`
- Test: `tests/test_mcp_subscriptions.py` (new)

- [ ] **Step 5.1.1: Write the failing test**

Create `tests/test_mcp_subscriptions.py`:

```python
from __future__ import annotations

from pathlib import Path

from src.mcp.subscriptions_store import SubscriptionStore
from src.mcp.models import Subscription


def test_store_create_and_list(tmp_path: Path):
    store = SubscriptionStore(tmp_path / "subs.json")
    sub = store.create(
        topic="AI inference",
        schedule="0 9 * * *",
        channels=["webhook"],
        config_pack=None,
    )
    assert isinstance(sub, Subscription)
    assert sub.topic == "AI inference"
    assert sub.active is True
    assert sub.id  # auto-generated UUID

    listed = store.list()
    assert len(listed) == 1
    assert listed[0].id == sub.id


def test_store_create_is_idempotent_on_topic(tmp_path: Path):
    store = SubscriptionStore(tmp_path / "subs.json")
    a = store.create(topic="AI", schedule="0 9 * * *", channels=["webhook"])
    b = store.create(topic="AI", schedule="0 10 * * *", channels=["webhook"])  # same topic
    assert a.id == b.id  # same record updated
    assert b.schedule == "0 10 * * *"  # schedule was updated
    assert len(store.list()) == 1


def test_store_delete_returns_true_for_existing(tmp_path: Path):
    store = SubscriptionStore(tmp_path / "subs.json")
    sub = store.create(topic="A", schedule="0 9 * * *", channels=["webhook"])
    assert store.delete(sub.id) is True
    assert store.list() == []


def test_store_delete_returns_false_for_missing(tmp_path: Path):
    store = SubscriptionStore(tmp_path / "subs.json")
    assert store.delete("nope") is False


def test_store_round_trips_through_file(tmp_path: Path):
    path = tmp_path / "subs.json"
    a = SubscriptionStore(path)
    a.create(topic="X", schedule="0 9 * * *", channels=["webhook"])

    b = SubscriptionStore(path)  # fresh instance reads from disk
    listed = b.list()
    assert len(listed) == 1
    assert listed[0].topic == "X"
```

- [ ] **Step 5.1.2: Run the test, verify failure**

```bash
uv run pytest tests/test_mcp_subscriptions.py -q
```
Expected: `ModuleNotFoundError: src.mcp.subscriptions_store`.

- [ ] **Step 5.1.3: Create `src/mcp/models.py`**

```python
"""MCP-server pydantic models."""
from __future__ import annotations

from datetime import datetime, timezone
from typing import List, Optional

from pydantic import BaseModel, Field


class Subscription(BaseModel):
    id: str
    topic: str
    schedule: str            # cron expression
    channels: List[str]      # e.g. ["webhook"], ["email"]
    config_pack: Optional[str] = None
    active: bool = True
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    last_run_at: Optional[datetime] = None
```

- [ ] **Step 5.1.4: Create `src/mcp/subscriptions_store.py`**

```python
"""File-backed CRUD store for topic subscriptions."""
from __future__ import annotations

import json
import uuid
from pathlib import Path
from typing import List, Optional

from .errors import HorizonMcpError
from .models import Subscription


_ALLOWED_CHANNELS = {"webhook", "email", "feishu", "slack"}


class SubscriptionStore:
    """JSON-file CRUD store. Idempotent by (normalized) topic."""

    def __init__(self, path: Path) -> None:
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def _load(self) -> List[Subscription]:
        if not self.path.exists():
            return []
        raw = json.loads(self.path.read_text(encoding="utf-8") or "[]")
        return [Subscription.model_validate(item) for item in raw]

    def _save(self, subs: List[Subscription]) -> None:
        payload = [json.loads(s.model_dump_json()) for s in subs]
        self.path.write_text(json.dumps(payload, indent=2, ensure_ascii=False),
                             encoding="utf-8")

    @staticmethod
    def _norm_topic(topic: str) -> str:
        return topic.strip().lower()

    def list(self) -> List[Subscription]:
        return self._load()

    def create(
        self,
        topic: str,
        schedule: str,
        channels: List[str],
        config_pack: Optional[str] = None,
    ) -> Subscription:
        if not topic.strip():
            raise HorizonMcpError(code="HZ_INVALID_INPUT", message="topic must be non-empty.")
        bad = [c for c in channels if c not in _ALLOWED_CHANNELS]
        if bad:
            raise HorizonMcpError(
                code="HZ_INVALID_INPUT",
                message=f"unknown channels: {bad}. Allowed: {sorted(_ALLOWED_CHANNELS)}.",
            )

        subs = self._load()
        target = self._norm_topic(topic)
        for existing in subs:
            if self._norm_topic(existing.topic) == target:
                # idempotent update
                existing.schedule = schedule
                existing.channels = channels
                existing.config_pack = config_pack
                existing.active = True
                self._save(subs)
                return existing

        sub = Subscription(
            id=str(uuid.uuid4()),
            topic=topic,
            schedule=schedule,
            channels=channels,
            config_pack=config_pack,
        )
        subs.append(sub)
        self._save(subs)
        return sub

    def delete(self, subscription_id: str) -> bool:
        subs = self._load()
        new_subs = [s for s in subs if s.id != subscription_id]
        if len(new_subs) == len(subs):
            return False
        self._save(new_subs)
        return True
```

- [ ] **Step 5.1.5: Add `data/subscriptions.json` to `.gitignore`**

Append to `.gitignore`:

```
data/subscriptions.json
```

- [ ] **Step 5.1.6: Run the tests, verify they pass**

```bash
uv run pytest tests/test_mcp_subscriptions.py -q
```
Expected: 5 passed.

- [ ] **Step 5.1.7: Commit**

```bash
git add src/mcp/models.py src/mcp/subscriptions_store.py .gitignore tests/test_mcp_subscriptions.py
git commit -m "feat(mcp): add Subscription model + file-backed CRUD store"
```

---

## Task 5.2 — Subscription Service Methods + MCP Tools

**Goal:** Wire the store into `HorizonPipelineService` and register three MCP tools: `hz_subscribe_topic`, `hz_list_subscriptions`, `hz_delete_subscription`.

**Files:**
- Modify: `src/mcp/service.py`
- Modify: `src/mcp/server.py`
- Test: `tests/test_mcp_subscriptions.py` (append)

- [ ] **Step 5.2.1: Write the failing test**

Append to `tests/test_mcp_subscriptions.py`:

```python
import asyncio
from src.mcp.service import HorizonPipelineService


def test_service_subscribe_round_trip(tmp_path):
    service = HorizonPipelineService(runs_root=tmp_path / "mcp-runs")
    service.subscriptions_path = tmp_path / "subs.json"
    service._subscription_store = None  # force re-init against custom path

    created = asyncio.run(service.subscribe_topic(
        topic="LLM inference",
        schedule="0 9 * * *",
        channels=["webhook"],
    ))
    assert created["topic"] == "LLM inference"

    listed = asyncio.run(service.list_subscriptions())
    assert listed["count"] == 1

    deleted = asyncio.run(service.delete_subscription(created["id"]))
    assert deleted["deleted"] is True

    listed2 = asyncio.run(service.list_subscriptions())
    assert listed2["count"] == 0


def test_hz_subscribe_topic_tool_envelope(tmp_path, monkeypatch):
    from src.mcp import server
    monkeypatch.setattr(server.service, "subscriptions_path", tmp_path / "subs.json")
    monkeypatch.setattr(server.service, "_subscription_store", None)

    result = asyncio.run(server.hz_subscribe_topic(
        topic="X", schedule="0 9 * * *", channels=["webhook"],
    ))
    assert result["ok"] is True
    assert result["tool"] == "hz_subscribe_topic"
    assert result["data"]["topic"] == "X"
```

- [ ] **Step 5.2.2: Run the tests, verify failure**

```bash
uv run pytest tests/test_mcp_subscriptions.py::test_service_subscribe_round_trip -q
```
Expected: `AttributeError` on `subscribe_topic` / `subscriptions_path`.

- [ ] **Step 5.2.3: Add subscription methods to `HorizonPipelineService`**

In `src/mcp/service.py`:

1. Add import:
   ```python
   from .subscriptions_store import SubscriptionStore
   ```
2. In `__init__`, after `self.briefing_cache = ...`:
   ```python
           self.subscriptions_path = self.runs_root.parent / "subscriptions.json"
           self._subscription_store: SubscriptionStore | None = None
   ```
3. Add the lazy property and three methods, e.g. after the `briefing_cache` line in the class but adjacent to similar lazy patterns:

```python
    @property
    def subscription_store(self) -> SubscriptionStore:
        if self._subscription_store is None:
            self._subscription_store = SubscriptionStore(self.subscriptions_path)
        return self._subscription_store

    async def subscribe_topic(
        self,
        topic: str,
        schedule: str = "0 9 * * *",
        channels: list[str] | None = None,
        config_pack: str | None = None,
    ) -> dict[str, Any]:
        ch = channels or ["webhook"]
        sub = self.subscription_store.create(
            topic=topic,
            schedule=schedule,
            channels=ch,
            config_pack=config_pack,
        )
        return json.loads(sub.model_dump_json())

    async def list_subscriptions(self) -> dict[str, Any]:
        subs = self.subscription_store.list()
        return {
            "count": len(subs),
            "items": [json.loads(s.model_dump_json()) for s in subs],
        }

    async def delete_subscription(self, subscription_id: str) -> dict[str, Any]:
        deleted = self.subscription_store.delete(subscription_id)
        return {"id": subscription_id, "deleted": deleted}
```

Add `import json` at the top of the file if not already present (it is — verify with `grep "^import json" src/mcp/service.py`; if missing, add).

- [ ] **Step 5.2.4: Register three MCP tools in `src/mcp/server.py`**

Insert after `hz_search_history`:

```python
@mcp.tool()
async def hz_subscribe_topic(
    topic: str,
    schedule: str = "0 9 * * *",
    channels: list[str] | None = None,
    config_pack: str | None = None,
) -> dict[str, Any]:
    """Create or update a topic subscription. Idempotent by topic."""

    return await _run_tool(
        "hz_subscribe_topic",
        lambda: service.subscribe_topic(
            topic=topic, schedule=schedule, channels=channels, config_pack=config_pack,
        ),
    )


@mcp.tool()
async def hz_list_subscriptions() -> dict[str, Any]:
    """List active topic subscriptions."""

    return await _run_tool(
        "hz_list_subscriptions",
        lambda: service.list_subscriptions(),
    )


@mcp.tool()
async def hz_delete_subscription(subscription_id: str) -> dict[str, Any]:
    """Delete a topic subscription by id."""

    return await _run_tool(
        "hz_delete_subscription",
        lambda: service.delete_subscription(subscription_id=subscription_id),
    )
```

- [ ] **Step 5.2.5: Run the tests, verify they pass**

```bash
uv run pytest tests/test_mcp_subscriptions.py -q
```

- [ ] **Step 5.2.6: Smoke check tool count**

```bash
uv run python scripts/check_mcp.py
```
Expected: `18 tools registered` (13 baseline + briefing + search + 3 subscriptions = 18).

- [ ] **Step 5.2.7: Commit**

```bash
git add src/mcp/service.py src/mcp/server.py tests/test_mcp_subscriptions.py
git commit -m "feat(mcp): register hz_subscribe_topic / hz_list_subscriptions / hz_delete_subscription"
```

**Day 5 Gate:** Subscribe + list + delete round-trips through MCP tool calls and persists to `data/subscriptions.json`.

---

## Task 6.1 — Config Pack Schema + Loader

**Files:**
- Create: `config_packs/SCHEMA.md`
- Modify: `src/mcp/horizon_adapter.py` (add `load_config_pack`)
- Test: `tests/test_mcp_config_packs.py` (new)

- [ ] **Step 6.1.1: Write the failing test**

Create `tests/test_mcp_config_packs.py`:

```python
from __future__ import annotations

import json
from pathlib import Path

import pytest

from src.mcp.horizon_adapter import load_config_pack
from src.mcp.errors import HorizonMcpError


def test_load_config_pack_returns_parsed_json(tmp_path, monkeypatch):
    packs_dir = tmp_path / "config_packs"
    packs_dir.mkdir()
    (packs_dir / "demo.json").write_text(json.dumps({
        "name": "Demo",
        "description": "d",
        "topic_keywords": ["a", "b"],
    }), encoding="utf-8")
    monkeypatch.setattr("src.mcp.horizon_adapter._CONFIG_PACKS_DIR", packs_dir)

    pack = load_config_pack("demo")
    assert pack["name"] == "Demo"
    assert pack["topic_keywords"] == ["a", "b"]


def test_load_config_pack_unknown_raises(tmp_path, monkeypatch):
    monkeypatch.setattr("src.mcp.horizon_adapter._CONFIG_PACKS_DIR", tmp_path / "nope")
    with pytest.raises(HorizonMcpError) as exc:
        load_config_pack("missing")
    assert exc.value.code == "HZ_INVALID_INPUT"


def test_load_config_pack_rejects_path_traversal(tmp_path, monkeypatch):
    monkeypatch.setattr("src.mcp.horizon_adapter._CONFIG_PACKS_DIR", tmp_path)
    with pytest.raises(HorizonMcpError):
        load_config_pack("../etc/passwd")
```

- [ ] **Step 6.1.2: Run, verify failure**

```bash
uv run pytest tests/test_mcp_config_packs.py -q
```
Expected: `ImportError: cannot import name 'load_config_pack'`.

- [ ] **Step 6.1.3: Implement `load_config_pack` in `src/mcp/horizon_adapter.py`**

Add near the top of `src/mcp/horizon_adapter.py`, after the existing constants:

```python
_CONFIG_PACKS_DIR = Path(__file__).resolve().parents[2] / "config_packs"
_CONFIG_PACK_NAME_RE = re.compile(r"^[a-z0-9][a-z0-9\-_]*$")
```

Add this function at the bottom of the file:

```python
def load_config_pack(name: str) -> dict[str, Any]:
    """Load a config pack JSON file by name.

    Pack name must match `^[a-z0-9][a-z0-9\-_]*$` (no path separators).
    Files live under repo-root/config_packs/<name>.json.
    """
    if not _CONFIG_PACK_NAME_RE.match(name or ""):
        raise HorizonMcpError(
            code="HZ_INVALID_INPUT",
            message=f"invalid config_pack name: {name!r}",
        )

    pack_path = _CONFIG_PACKS_DIR / f"{name}.json"
    if not pack_path.exists():
        raise HorizonMcpError(
            code="HZ_INVALID_INPUT",
            message=f"config_pack not found: {name}",
            details={"checked": str(pack_path)},
        )
    with pack_path.open("r", encoding="utf-8") as fh:
        return json.load(fh)
```

- [ ] **Step 6.1.4: Create `config_packs/SCHEMA.md`**

```markdown
# Config Pack Schema

Config packs are turnkey JSON bundles that extend the base `data/config.json` schema with vertical-specific defaults.

Each pack must contain:

| Field | Type | Required | Notes |
|---|---|:---:|---|
| `name` | string | ✅ | Human-readable name. Shown in UI |
| `description` | string | ✅ | One-line description |
| `topic_keywords` | string[] | ✅ | Default keyword bundle for `hz_get_briefing` |
| `sources` | object | ✅ | Same shape as `data/config.json` sources |
| `filtering.ai_score_threshold` | number | ❌ | Override; default 7.0 |
| `scoring_prompt_addendum` | string | ❌ | Extra instructions appended to `CONTENT_ANALYSIS_USER` |

Pack file name must match `^[a-z0-9][a-z0-9\-_]*$` (no path separators, no uppercase). Place under `config_packs/<name>.json` with a sibling `<name>.README.md`.
```

- [ ] **Step 6.1.5: Run the tests, verify they pass**

```bash
uv run pytest tests/test_mcp_config_packs.py -q
```

- [ ] **Step 6.1.6: Commit**

```bash
git add src/mcp/horizon_adapter.py config_packs/SCHEMA.md tests/test_mcp_config_packs.py
git commit -m "feat(mcp): add load_config_pack helper + schema doc"
```

---

## Task 6.2 — Ship Three Config Pack JSONs

**Goal:** Three production packs. Each must validate against the schema in Task 6.1 and produce a usable briefing.

**Files:**
- Create: `config_packs/ai-developers.json` + `.README.md`
- Create: `config_packs/livestream-compliance.json` + `.README.md`
- Create: `config_packs/overseas-policy.json` + `.README.md`
- Test: `tests/test_mcp_config_packs.py` (append)

- [ ] **Step 6.2.1: Write the failing test**

Append to `tests/test_mcp_config_packs.py`:

```python
import json
from pathlib import Path


PACKS_DIR = Path(__file__).resolve().parents[1] / "config_packs"


def test_ai_developers_pack_is_valid():
    pack = json.loads((PACKS_DIR / "ai-developers.json").read_text(encoding="utf-8"))
    assert pack["name"]
    assert pack["description"]
    assert len(pack["topic_keywords"]) >= 5
    assert isinstance(pack["sources"], dict)


def test_livestream_compliance_pack_is_valid():
    pack = json.loads((PACKS_DIR / "livestream-compliance.json").read_text(encoding="utf-8"))
    assert pack["name"]
    assert len(pack["topic_keywords"]) >= 5
    assert isinstance(pack["sources"], dict)


def test_overseas_policy_pack_is_valid():
    pack = json.loads((PACKS_DIR / "overseas-policy.json").read_text(encoding="utf-8"))
    assert pack["name"]
    assert len(pack["topic_keywords"]) >= 5
    assert isinstance(pack["sources"], dict)


def test_all_three_packs_have_readmes():
    for name in ["ai-developers", "livestream-compliance", "overseas-policy"]:
        assert (PACKS_DIR / f"{name}.README.md").exists(), f"missing README for {name}"
```

- [ ] **Step 6.2.2: Run, verify failure**

```bash
uv run pytest tests/test_mcp_config_packs.py -q
```
Expected: 4 FileNotFoundErrors.

- [ ] **Step 6.2.3: Write `config_packs/ai-developers.json`**

```json
{
  "name": "AI Developers",
  "description": "Curated for engineers working with Claude / Cursor / Codex / open-source LLM tooling.",
  "topic_keywords": [
    "llm", "inference", "claude", "anthropic", "openai", "cursor",
    "vllm", "sglang", "triton", "cuda", "rag", "agent"
  ],
  "sources": {
    "github": [
      {"type": "user_events", "username": "karpathy", "enabled": true},
      {"type": "user_events", "username": "simonw", "enabled": true},
      {"type": "repo_releases", "owner": "vllm-project", "repo": "vllm", "enabled": true},
      {"type": "repo_releases", "owner": "sgl-project", "repo": "sglang", "enabled": true},
      {"type": "repo_releases", "owner": "anthropics", "repo": "claude-code", "enabled": true}
    ],
    "rss": [
      {"name": "Anthropic News", "url": "https://www.anthropic.com/news/rss.xml", "enabled": true},
      {"name": "Simon Willison", "url": "https://simonwillison.net/atom/everything/", "enabled": true}
    ],
    "hackernews": {"min_score": 100, "enabled": true},
    "reddit": [
      {"subreddit": "LocalLLaMA", "min_score": 50, "enabled": true},
      {"subreddit": "ClaudeAI", "min_score": 20, "enabled": true}
    ]
  },
  "filtering": {"ai_score_threshold": 7.5},
  "scoring_prompt_addendum": "Bias toward content useful for engineers shipping LLM-powered software."
}
```

- [ ] **Step 6.2.4: Write `config_packs/ai-developers.README.md`**

```markdown
# AI Developers Config Pack

For engineers using Claude / Cursor / Codex and shipping LLM-powered software.

## Sources
- GitHub: karpathy + simonw user activity; vllm / sglang / claude-code releases
- RSS: Anthropic news, Simon Willison's blog
- HackerNews (score ≥ 100), r/LocalLLaMA, r/ClaudeAI

## Default Topic Keywords
`llm`, `inference`, `claude`, `anthropic`, `openai`, `cursor`, `vllm`, `sglang`, `triton`, `cuda`, `rag`, `agent`

## Threshold
`ai_score_threshold = 7.5` (slightly stricter than default 7.0 — high-signal pack).

## Usage
```python
hz_get_briefing(topic="LLM inference", config_pack="ai-developers", hours=24, count=5)
```
```

- [ ] **Step 6.2.5: Write `config_packs/livestream-compliance.json`**

```json
{
  "name": "直播电商合规",
  "description": "中国直播电商商家/服务商的合规规则跟踪：抖音/快手/视频号/天猫/京东及监管动态。",
  "topic_keywords": [
    "合规", "处罚", "封号", "类目", "结算", "退款", "直播", "抖音", "快手", "samr", "市监", "电商法"
  ],
  "sources": {
    "rss": [
      {"name": "国家市监总局-市场监管动态", "url": "https://www.samr.gov.cn/rss.xml", "enabled": true}
    ],
    "telegram": [
      {"channel": "ecom_compliance_cn", "enabled": true}
    ]
  },
  "filtering": {"ai_score_threshold": 7.0},
  "scoring_prompt_addendum": "重点关注是否涉及处罚机制、商家资质、结算/退款规则变更。"
}
```

- [ ] **Step 6.2.6: Write `config_packs/livestream-compliance.README.md`**

```markdown
# 直播电商合规 Config Pack

为中国直播电商商家与服务商跟踪监管/平台合规动态。

## Sources
- RSS: SAMR 市场监管总局
- Telegram: `@ecom_compliance_cn`（社区维护）

> **维护说明**：直播平台官方公告大多不提供稳定 RSS。如需抖音/快手学习中心 RSS，请在 `data/config.json` 中补充自建抓取脚本，再 merge 进本 pack。

## Default Topic Keywords
合规、处罚、封号、类目、结算、退款、直播、抖音、快手、samr、市监、电商法

## Usage
```python
hz_get_briefing(topic="抖音处罚", config_pack="livestream-compliance", language="zh", hours=48)
```
```

- [ ] **Step 6.2.7: Write `config_packs/overseas-policy.json`**

```json
{
  "name": "Overseas Platform Policy",
  "description": "Tracking TikTok / Shopify / Stripe / FTC policy changes affecting cross-border e-commerce.",
  "topic_keywords": [
    "tiktok", "shopify", "stripe", "ftc", "ban", "policy", "shop", "ads", "kyc", "sanctions"
  ],
  "sources": {
    "rss": [
      {"name": "TikTok Newsroom", "url": "https://newsroom.tiktok.com/en-us/rss", "enabled": true},
      {"name": "Shopify Blog", "url": "https://www.shopify.com/blog.atom", "enabled": true},
      {"name": "Stripe Blog", "url": "https://stripe.com/blog/feed.rss", "enabled": true},
      {"name": "FTC Press Releases", "url": "https://www.ftc.gov/news-events/news/press-releases/rss", "enabled": true}
    ]
  },
  "filtering": {"ai_score_threshold": 7.0},
  "scoring_prompt_addendum": "Prioritize policy changes that affect cross-border sellers and payment flows."
}
```

- [ ] **Step 6.2.8: Write `config_packs/overseas-policy.README.md`**

```markdown
# Overseas Platform Policy Config Pack

Tracks policy/regulation changes from TikTok, Shopify, Stripe, and the US FTC — relevant for cross-border e-commerce operators.

## Sources
- TikTok Newsroom RSS
- Shopify Blog Atom feed
- Stripe Blog RSS
- FTC Press Releases RSS

## Default Topic Keywords
`tiktok`, `shopify`, `stripe`, `ftc`, `ban`, `policy`, `shop`, `ads`, `kyc`, `sanctions`

## Usage
```python
hz_get_briefing(topic="TikTok policy", config_pack="overseas-policy", hours=72)
```
```

- [ ] **Step 6.2.9: Run all config pack tests**

```bash
uv run pytest tests/test_mcp_config_packs.py -q
```
Expected: all green.

- [ ] **Step 6.2.10: Commit**

```bash
git add config_packs/ tests/test_mcp_config_packs.py
git commit -m "feat(config-packs): ship ai-developers, livestream-compliance, overseas-policy"
```

---

## Task 6.3 — Wire `config_pack` Through `hz_get_briefing` + `hz_subscribe_topic`

**Goal:** When `config_pack` is provided, merge its `topic_keywords` + `filtering.ai_score_threshold` + `scoring_prompt_addendum` into the briefing's effective parameters. Subscription store stores the `config_pack` name (already done in Task 5.1), so this task only changes the briefing path.

**Files:**
- Modify: `src/mcp/service.py` (`get_briefing` consumes config pack)
- Test: `tests/test_mcp_config_packs.py` (append)

- [ ] **Step 6.3.1: Write the failing test**

Append to `tests/test_mcp_config_packs.py`:

```python
import asyncio
from src.mcp.service import HorizonPipelineService


def test_get_briefing_merges_config_pack_keywords(tmp_path, monkeypatch):
    fake_pack = {
        "name": "x",
        "description": "x",
        "topic_keywords": ["vllm", "triton"],
        "sources": {},
        "filtering": {"ai_score_threshold": 8.0},
    }
    monkeypatch.setattr("src.mcp.service.load_config_pack", lambda name: fake_pack)

    captured_kwargs = {}

    async def fake_run_pipeline(self, **kwargs):
        captured_kwargs.update(kwargs)
        return {"run_id": "r", "fetch": {}, "score": {}, "filter": {},
                "enrich": {}, "summaries": [], "meta": {}}

    monkeypatch.setattr(HorizonPipelineService, "run_pipeline", fake_run_pipeline)
    monkeypatch.setattr(HorizonPipelineService, "get_run_stage",
                        lambda self, **kw: {"items": []})

    service = HorizonPipelineService(runs_root=tmp_path / "mcp-runs")
    asyncio.run(service.get_briefing(topic="LLM", config_pack="demo"))

    kws = captured_kwargs["topic_keywords"]
    assert "llm" in kws         # from topic
    assert "vllm" in kws        # from pack
    assert "triton" in kws      # from pack
    assert captured_kwargs["threshold"] == 8.0  # pack overrode min_score


def test_get_briefing_without_config_pack_unchanged(tmp_path, monkeypatch):
    captured_kwargs = {}

    async def fake_run_pipeline(self, **kwargs):
        captured_kwargs.update(kwargs)
        return {"run_id": "r", "fetch": {}, "score": {}, "filter": {},
                "enrich": {}, "summaries": [], "meta": {}}

    monkeypatch.setattr(HorizonPipelineService, "run_pipeline", fake_run_pipeline)
    monkeypatch.setattr(HorizonPipelineService, "get_run_stage",
                        lambda self, **kw: {"items": []})

    service = HorizonPipelineService(runs_root=tmp_path / "mcp-runs")
    asyncio.run(service.get_briefing(topic="LLM"))
    assert captured_kwargs["threshold"] == 7.0  # default min_score
```

- [ ] **Step 6.3.2: Run, verify failure**

```bash
uv run pytest tests/test_mcp_config_packs.py::test_get_briefing_merges_config_pack_keywords -q
```
Expected: assertion failure — `"vllm"` not in kws.

- [ ] **Step 6.3.3: Update `get_briefing` in `src/mcp/service.py`**

Add import at top of `src/mcp/service.py`:

```python
from .horizon_adapter import load_config_pack as _load_config_pack
load_config_pack = _load_config_pack  # exposed for monkeypatching in tests
```

In `get_briefing`, between the validation block and the cache lookup, insert:

```python
        pack_keywords: list[str] = []
        effective_min_score = min_score
        if config_pack:
            pack = load_config_pack(config_pack)
            pack_keywords = list(pack.get("topic_keywords") or [])
            pack_threshold = (pack.get("filtering") or {}).get("ai_score_threshold")
            if pack_threshold is not None:
                effective_min_score = float(pack_threshold)
```

Replace the existing `keywords = _topic_to_keywords(topic)` line with a merge:

```python
        topic_kw = _topic_to_keywords(topic)
        seen: set[str] = set()
        keywords = [k for k in topic_kw + [pk.lower() for pk in pack_keywords]
                    if not (k in seen or seen.add(k))]
```

Replace `threshold=min_score` in the `run_pipeline` call with `threshold=effective_min_score`, and also use it in the cache key:

```python
        cache_key = CacheKey(
            tenant_id="default",
            topic=topic.strip().lower(),
            language=language,
            hours=hours,
            min_score=effective_min_score,
            config_pack=config_pack,
        )
```

- [ ] **Step 6.3.4: Run, verify all green**

```bash
uv run pytest tests/test_mcp_config_packs.py tests/test_mcp_briefing.py -q
```

- [ ] **Step 6.3.5: End-to-end manual smoke (real network, expects API keys set)**

```bash
uv run python -c "
import asyncio
from src.mcp.service import HorizonPipelineService
service = HorizonPipelineService()
result = asyncio.run(service.get_briefing(
    topic='LLM inference', config_pack='ai-developers', count=3, language='en'))
print(f'item_count={result[\"item_count\"]}, cached={result[\"cached\"]}')
for it in result['items']:
    print(f'  [{it[\"rank\"]}] {it[\"score\"]:.1f} {it[\"title\"]}')
"
```
Expected: at least 1 item printed (more realistic: 3+). If it fails because of missing API keys, log this and continue — that's a Phase 2 concern.

- [ ] **Step 6.3.6: Commit**

```bash
git add src/mcp/service.py tests/test_mcp_config_packs.py
git commit -m "feat(mcp): hz_get_briefing merges config_pack keywords and threshold"
```

**Day 6 Gate:** All three packs load via `load_config_pack`, their keywords merge into briefing requests, and tests for the merge logic are green.

---

## Task 7.1 — Update `src/mcp/README.md` Tool Table

**Goal:** README reflects the 5 new tools (`hz_get_briefing`, `hz_search_history`, `hz_subscribe_topic`, `hz_list_subscriptions`, `hz_delete_subscription`) and the `topic_keywords` param on `hz_run_pipeline` / `hz_score_items`.

**Files:**
- Modify: `src/mcp/README.md`

- [ ] **Step 7.1.1: Read the current tool table**

```bash
grep -n "^|" src/mcp/README.md | head -40
```

Identify the tool table boundary lines and column headers.

- [ ] **Step 7.1.2: Edit the tool table**

Add these rows in the appropriate alphabetical/grouping order — surface them grouped under a new heading "### One-call & topic tools" right after the existing staged-pipeline tools. Use the existing column layout. For each new tool, include: name, brief description, key params.

Example block to insert (adapt formatting to match existing table style):

```markdown
### One-call & topic tools

| Tool | Purpose | Key params |
|---|---|---|
| `hz_get_briefing` | Top-N curated items on a topic with cache | `topic`, `hours`, `count`, `language`, `min_score`, `force_refresh`, `config_pack` |
| `hz_search_history` | Keyword + date-range search over enriched history | `query`, `days`, `top_k`, `min_score` |
| `hz_subscribe_topic` | Create or update a topic subscription | `topic`, `schedule`, `channels`, `config_pack` |
| `hz_list_subscriptions` | List active subscriptions | — |
| `hz_delete_subscription` | Delete a subscription by id | `subscription_id` |

### Topic-aware params (additive, all backward-compatible)

`hz_run_pipeline` and `hz_score_items` now accept an optional `topic_keywords: list[str]` parameter. When supplied, scoring prompts include a `Topic relevance` dimension so high-score items skew toward the topic.

### Config packs

Three turnkey vertical bundles ship in `config_packs/`:
- `ai-developers` — LLM/inference engineers
- `livestream-compliance` — 中国直播电商合规
- `overseas-policy` — TikTok/Stripe/FTC cross-border policy

Pass `config_pack="<name>"` to `hz_get_briefing` or `hz_subscribe_topic` to apply.
```

- [ ] **Step 7.1.3: Commit**

```bash
git add src/mcp/README.md
git commit -m "docs(mcp): document new tools, topic_keywords, config packs"
```

---

## Task 7.2 — Closeout: Full Suite + Tag

**Files:** none (CI / git operations only)

- [ ] **Step 7.2.1: Run full test suite**

```bash
uv run pytest -q
```
Expected: all green. Note the total count.

- [ ] **Step 7.2.2: Run check_mcp**

```bash
uv run python scripts/check_mcp.py
```
Expected: `18 tools registered` (verified in Task 5.2).

- [ ] **Step 7.2.3: Manual demo from Claude Desktop (or any MCP client)**

Wire local stdio config and invoke each of the 5 new tools at least once. Confirm responses match the documented shapes. If running the briefing requires real API keys, OK to skip if env not set — but at minimum confirm the tool registers and rejects bad inputs.

- [ ] **Step 7.2.4: Tag v0.1.0-mcp-week1**

```bash
git tag -a v0.1.0-mcp-week1 -m "Horizon MCP — Phase 1 (tools + config packs) complete

- hz_get_briefing with cache
- hz_search_history
- hz_subscribe_topic / list / delete (file-backed)
- topic_keywords threaded through analyzer + pipeline
- 3 vertical config packs: ai-developers, livestream-compliance, overseas-policy
"
```

(Do not push the tag unless the user requests it explicitly — Day 7 of the larger sprint is a public update day but this plan stops at engineering completion.)

- [ ] **Step 7.2.5: Final commit (only if pending changes)**

```bash
git status
```
If clean, this step is a no-op. Otherwise: investigate, do not bypass.

**Day 7 Gate:** Full suite green, `check_mcp` reports 18 tools, tag exists locally.

---

## Self-Review Notes

**Spec coverage check (against `docs/COMMERCIAL_SPEC.md` §3, §4):**

| Spec requirement | Task covering it |
|---|---|
| §3.1 `hz_get_briefing` MVP | Task 1.2, 1.3 |
| §3.1 Briefing cache (LRU) | Task 2.1, 2.2 |
| §3.1 `force_refresh` / `cached` fields | Task 2.2 |
| §3.2 `hz_search_history` keyword + date filter | Task 3.1, 3.2 |
| §3.3 `hz_subscribe_topic` + `hz_list_subscriptions` | Task 5.1, 5.2 (also adds `hz_delete_subscription` for completeness) |
| §3.4 `topic_keywords` on `filter_items` / `run_pipeline` | Task 4.2 |
| §3.4 `<topic_relevance>` scoring prompt dimension | Task 4.1 |
| §4.1–4.3 Three config packs + `load_config_pack` merge | Task 6.1, 6.2, 6.3 |

**Out of Phase 1 scope (covered by later plans, do NOT add here):**
- Schedule executor for subscriptions (Phase 2 alongside HTTP deployment)
- Email / Feishu / Slack channel adapters (Phase 5)
- Postgres migration of briefings + subscriptions (Phase 3)
- Multi-tenant `tenant_id` propagation (Phase 4) — only the cache key shape is forward-compatible
- Public landing page (Phase 6)

**Backward-compatibility guarantees verified:**
- `test_analyze_batch_without_topic_keywords_does_not_change_prompt` (Task 4.1)
- `test_score_items_without_topic_keywords_passes_none` (Task 4.2)
- Existing `tests/test_mcp_service_smoke.py`, `tests/test_mcp_adapter.py`, etc. unchanged and re-run after every commit

---

## Execution Handoff

Two execution options:

**1. Subagent-Driven (recommended)** — Dispatch a fresh subagent per task; review checkpoint between tasks; fastest iteration.

**2. Inline Execution** — Execute tasks in this session via `superpowers:executing-plans`; batch with checkpoints.

Pick one and continue.
