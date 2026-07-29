# Horizon MCP · Commercial Spec

> Engineering spec for productizing the existing Horizon MCP server (`src/mcp/`) into a paid SaaS over a 14-day sprint.
> Companion business doc lives in the personal Obsidian vault at `side-hustles/Project-G-Horizon情报引擎/04 - MCP 商业化 spec.md`.
> This file is the source of truth for Claude Code execution.

**Status**: Draft · **Sprint start**: TBD · **Sprint length**: 14 days
**Owner**: Defang · **Last updated**: 2026-05-21

---

## 1. Goal & Non-Goals

### 1.1 Goal
Ship a paid, remote-hosted version of `src/mcp/` within 14 days, accepting Stripe + WeChat Pay subscriptions, with a documented set of "finished-product" tools that wrap the existing pipeline (fetch → score → filter → enrich → summarize) into one-call workflows.

### 1.2 Non-Goals
- Do not rewrite Horizon business logic. New tools wrap `service.HorizonPipelineService`.
- Do not replace file-based `data/mcp-runs/` for self-hosted users. Postgres is additive.
- Do not ship vector search in this sprint. Keyword search + filter is enough for MVP. Vector RAG goes to Phase 2.
- Do not build a web app. Landing page is a static GitHub Pages section. All real interaction is in the MCP client.

---

## 2. Current State (as of 2026-05-21)

| Layer | Files | Status |
|---|---|---|
| MCP server | `src/mcp/server.py` (504 LOC) | 13 tools, 7 resources, FastMCP stdio transport |
| Service | `src/mcp/service.py` (649 LOC) | All pipeline stages wired |
| Adapter | `src/mcp/horizon_adapter.py` (322 LOC) | Reuses orchestrator + scrapers + ai |
| Storage | `src/mcp/run_store.py` (133 LOC) | File-based artifacts under `data/mcp-runs/` |
| Docs | `src/mcp/README.md`, `src/mcp/integration.md` | Client config examples included |

Existing tools (do not remove or rename):
`hz_validate_config`, `hz_fetch_items`, `hz_score_items`, `hz_filter_items`, `hz_enrich_items`, `hz_generate_summary`, `hz_run_pipeline`, `hz_list_runs`, `hz_get_run_meta`, `hz_get_run_stage`, `hz_get_run_summary`, `hz_get_metrics`, `hz_send_webhook`.

---

## 3. New Tools (P0)

### 3.1 `hz_get_briefing`

The single most important new tool. Wraps `run_pipeline` for one-call "give me today's curated items on topic X".

**Signature** (`src/mcp/server.py` + `service.py`):

```python
@mcp.tool()
async def hz_get_briefing(
    topic: str,
    hours: int = 24,
    count: int = 5,
    language: str = "zh",          # "zh" | "en"
    min_score: float = 7.0,
    use_cache: bool = True,
    force_refresh: bool = False,
    config_pack: str | None = None,  # "ai-developers" | "livestream-compliance" | "overseas-policy"
    horizon_path: str | None = None,
    config_path: str | None = None,
) -> dict[str, Any]:
    """Return a curated briefing of top-N items on a topic.

    Internally calls service.get_briefing(...) which:
      1. Checks briefing cache (60-min TTL by default)
      2. On cache miss: runs the existing pipeline with topic_keywords filter
      3. Returns ranked items with summary + enriched context
    """
```

**Response schema**:

```jsonc
{
  "ok": true,
  "tool": "hz_get_briefing",
  "data": {
    "topic": "AI inference",
    "language": "zh",
    "time_window_hours": 24,
    "cached": false,
    "run_id": "20260521-091523",
    "item_count": 5,
    "items": [
      {
        "rank": 1,
        "title": "...",
        "url": "...",
        "source": "hackernews",
        "score": 9.2,
        "summary": "...",        // Chinese or English per `language`
        "context": "...",         // from enricher
        "comments_digest": "..."  // optional, from enricher
      }
    ]
  },
  "meta": { "timestamp": "2026-05-21T09:15:23Z", "duration_ms": 4123.5 }
}
```

**Implementation notes**:
- Add `async def get_briefing(...)` to `HorizonPipelineService` (~80 LOC).
- Cache via a new `src/mcp/cache.py` (LRU in-memory for MVP, swap to Postgres `briefings` table on Day 9).
- Reuse `run_pipeline` internals: pass `topic_keywords=[topic, ...]` derived from the topic string; if `config_pack` is set, merge its keyword bundle.
- Default `enrich=True`, `topic_dedup=True`.

### 3.2 `hz_search_history`

```python
@mcp.tool()
async def hz_search_history(
    query: str,
    days: int = 30,
    top_k: int = 10,
    min_score: float = 7.0,
    horizon_path: str | None = None,
    config_path: str | None = None,
) -> dict[str, Any]:
    """Keyword + date-range search over historical run artifacts."""
```

- MVP impl: iterate `RunStore.list_runs()` within window, ILIKE-match title/summary, sort by score.
- After Day 9 (Postgres): rewrite as a `SELECT ... WHERE` with GIN index on `runs.data`.
- Vector search deferred to Phase 2.

### 3.3 `hz_subscribe_topic` & `hz_list_subscriptions`

```python
@mcp.tool()
async def hz_subscribe_topic(
    topic: str,
    schedule: str = "0 9 * * *",        # cron
    channels: list[str] = ["email"],    # email | feishu | slack | webhook
    config_pack: str | None = None,
    horizon_path: str | None = None,
) -> dict[str, Any]:
    """Create or update a topic subscription."""

@mcp.tool()
async def hz_list_subscriptions() -> dict[str, Any]:
    """List active subscriptions for the current tenant."""
```

- MVP storage: `data/subscriptions.json` (Day 5)
- Day 10 migrate to Postgres `topic_subscriptions` table
- Schedule executor: a Fly.io `[processes]` worker (separate from web), reads cron, invokes `hz_get_briefing`, then `hz_send_webhook` / SMTP

### 3.4 Enhance existing tools with `topic_keywords`

Modify (do not break existing callers — keep param optional):

- `service.HorizonPipelineService.filter_items(... , topic_keywords: list[str] | None = None)`
- `service.HorizonPipelineService.run_pipeline(... , topic_keywords: list[str] | None = None)`
- `service.HorizonPipelineService.get_briefing(...)` passes `topic_keywords` derived from `topic`

Scoring prompt (probably in `src/ai/scoring.py`): add a `<topic_relevance>` dimension. Backwards-compatible:
- If `topic_keywords` is None, score prompt is identical to current behavior.
- If set, prompt instructs the model to weight relevance to topic alongside intrinsic quality.

---

## 4. Config Packs

Three vertical bundles ship in this sprint. Stored under a new directory `config_packs/`.

### 4.1 Directory layout
```
config_packs/
  ai-developers.json
  ai-developers.README.md
  livestream-compliance.json
  livestream-compliance.README.md
  overseas-policy.json
  overseas-policy.README.md
```

### 4.2 Schema
Each `.json` extends `data/config.json` schema with extra fields:
```jsonc
{
  "name": "AI Developers",
  "description": "Curated for engineers using Claude / Cursor / Codex.",
  "topic_keywords": ["llm", "inference", "cuda", "vllm", "anthropic", "openai", ...],
  "rss": [...],
  "reddit": [...],
  "hackernews": { ... },
  "telegram": [...],
  "github": [...],
  "scoring_prompt_addendum": "...",
  "filtering": { "ai_score_threshold": 7.5 }
}
```

### 4.3 Resolution
- New helper in `horizon_adapter.py`: `def load_config_pack(name: str) -> dict`
- Merge order: base config → config_pack → CLI/tool overrides

---

## 5. Remote MCP Transport

### 5.1 New entrypoint `src/mcp/server_http.py`

```python
"""HTTP transport for Horizon MCP (production)."""
from mcp.server.fastmcp import FastMCP
from .server import mcp  # reuse all tool registrations

# Wrap with middleware (added in §6)
def main() -> None:
    mcp.run(transport="streamable-http", host="0.0.0.0", port=8080)

if __name__ == "__main__":
    main()
```

Add to `pyproject.toml`:
```toml
[project.scripts]
horizon-mcp = "src.mcp.server:main"
horizon-mcp-http = "src.mcp.server_http:main"
```

### 5.2 Fly.io config `fly.toml`
```toml
app = "horizon-mcp"
primary_region = "iad"

[build]
dockerfile = "Dockerfile"

[[services]]
internal_port = 8080
protocol = "tcp"

  [[services.ports]]
  port = 80
  handlers = ["http"]

  [[services.ports]]
  port = 443
  handlers = ["tls", "http"]

  [services.concurrency]
  type = "connections"
  hard_limit = 50
  soft_limit = 25

[[services.http_checks]]
path = "/healthz"
interval = "15s"
timeout = "5s"

[processes]
app = "horizon-mcp-http"
scheduler = "python -m src.scheduler.runner"
```

### 5.3 Dockerfile update
Existing `Dockerfile` likely runs `horizon-mcp` (stdio). Update entrypoint to `horizon-mcp-http`, expose 8080.

### 5.4 Client config example
```jsonc
{
  "mcpServers": {
    "horizon": {
      "url": "https://horizon-mcp.fly.dev/mcp",
      "headers": { "Authorization": "Bearer sk_horizon_xxxxx" }
    }
  }
}
```

---

## 6. Auth, Quota, Multi-tenant

### 6.1 Postgres schema (Supabase)

```sql
CREATE TABLE tenants (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  api_key TEXT UNIQUE NOT NULL,
  email TEXT,
  plan TEXT NOT NULL DEFAULT 'free',  -- free|pro|team|enterprise
  quota_limit INT NOT NULL DEFAULT 50,
  quota_used INT NOT NULL DEFAULT 0,
  quota_reset_at TIMESTAMPTZ NOT NULL DEFAULT (now() + interval '30 days'),
  created_at TIMESTAMPTZ DEFAULT now()
);
CREATE INDEX idx_tenants_api_key ON tenants (api_key);

CREATE TABLE subscriptions (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  tenant_id UUID REFERENCES tenants(id) ON DELETE CASCADE,
  provider TEXT NOT NULL,             -- stripe | wechatpay
  external_id TEXT NOT NULL,
  status TEXT NOT NULL,
  current_period_end TIMESTAMPTZ NOT NULL,
  created_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE runs (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  tenant_id UUID REFERENCES tenants(id) ON DELETE CASCADE,
  run_id TEXT NOT NULL,
  stage TEXT NOT NULL,                -- raw|scored|filtered|enriched
  data JSONB NOT NULL,
  created_at TIMESTAMPTZ DEFAULT now(),
  UNIQUE (tenant_id, run_id, stage)
);
CREATE INDEX idx_runs_tenant_run ON runs (tenant_id, run_id);

CREATE TABLE briefings (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  tenant_id UUID REFERENCES tenants(id) ON DELETE CASCADE,
  topic TEXT NOT NULL,
  language TEXT NOT NULL,
  items JSONB NOT NULL,
  cached_until TIMESTAMPTZ NOT NULL,
  created_at TIMESTAMPTZ DEFAULT now()
);
CREATE INDEX idx_briefings_lookup ON briefings (tenant_id, topic, language, cached_until);

CREATE TABLE topic_subscriptions (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  tenant_id UUID REFERENCES tenants(id) ON DELETE CASCADE,
  topic TEXT NOT NULL,
  schedule TEXT NOT NULL,
  channels JSONB NOT NULL,
  config_pack TEXT,
  active BOOLEAN DEFAULT true,
  last_run_at TIMESTAMPTZ,
  created_at TIMESTAMPTZ DEFAULT now()
);
```

### 6.2 Middleware
New directory `src/mcp/middleware/`:

```python
# src/mcp/middleware/auth.py
async def auth_middleware(request, call_next):
    api_key = _extract_bearer(request)
    if not api_key:
        return _401("missing api key")
    tenant = await tenants_repo.fetch_by_key(api_key)
    if not tenant:
        return _401("invalid api key")
    request.state.tenant = tenant
    return await call_next(request)

# src/mcp/middleware/quota.py
async def quota_middleware(request, call_next):
    tenant = request.state.tenant
    if tenant.plan in ("free", "pro"):
        if tenant.quota_used >= tenant.quota_limit:
            return _429(f"quota exceeded: {tenant.quota_used}/{tenant.quota_limit}")
    response = await call_next(request)
    if response.status_code < 400:
        await tenants_repo.increment_quota(tenant.id)
    return response
```

### 6.3 Plan → Quota table
| Plan | Monthly limit |
|---|---|
| free | 50 |
| pro | 500 |
| team | unlimited (soft cap 10k for abuse) |
| enterprise | unlimited |

---

## 7. Billing

### 7.1 Stripe (USD)
- Stripe Checkout for upgrade
- Webhook endpoint `/webhook/stripe`
- Handle events: `checkout.session.completed`, `customer.subscription.updated`, `customer.subscription.deleted`
- On `completed`: lookup tenant by email → update plan + quota_limit + create `subscriptions` row

### 7.2 WeChat Pay (CNY)
- Use [pingxx](https://pingxx.com) or [z-pay](https://z-pay.cn) — choose simplest onboarding
- Webhook endpoint `/webhook/wechatpay`
- Same downstream behavior as Stripe webhook

### 7.3 Pricing (write into landing page)
| Plan | USD | CNY |
|---|---|---|
| Free | $0 | ¥0 |
| Pro | $19/mo | ¥99/mo |
| Team | $99/mo | ¥499/mo |
| Enterprise | $500+/mo | ¥3,000+/mo |

---

## 8. Observability

- Add Sentry SDK init at `src/mcp/server_http.py` entry (env `SENTRY_DSN`)
- Keep existing `METRICS` dict but back it with Postgres on Day 9 for cross-restart durability
- `/healthz` endpoint returning `{"status": "ok", "version": <git_sha>}`
- Fly.io built-in logs + metrics dashboard

---

## 9. 14-Day Sprint Plan

Each day has a deliverable and a Gate. Do not proceed if Gate fails.

### Week 1 — Tools & Config Packs

#### Day 1: `hz_get_briefing` MVP
- Files: `src/mcp/service.py`, `src/mcp/server.py`, `tests/mcp/test_get_briefing.py` (new)
- Implementation: ~80 LOC service method + 25 LOC tool registration
- **Gate**: `uv run python scripts/check_mcp.py` passes; new test green

#### Day 2: Briefing cache layer
- Files: `src/mcp/cache.py` (new, ~60 LOC, LRU 256 entries)
- Add `cached_until: datetime` to briefing response
- **Gate**: Calling same `(topic, hours, language)` twice within 60 min returns `cached=true`

#### Day 3: `hz_search_history` MVP
- Files: `src/mcp/service.py` (`search_history` method), `src/mcp/server.py` (tool reg)
- Impl: iterate `RunStore.list_runs()`, ILIKE on title + summary, sort by score
- **Gate**: With 3 days of historical runs, can return relevant items for a known keyword

#### Day 4: `topic_keywords` integration
- Modify `service.filter_items`, `service.run_pipeline` signatures (optional param, backwards compatible)
- Modify scoring prompt in `src/ai/scoring.py` (or wherever AI scoring prompt is built) to add `<topic_relevance>` dimension only when `topic_keywords` passed
- **Gate**: Same source set, with topic_keywords vs without → high-score items shift toward topic

#### Day 5: `hz_subscribe_topic` MVP (file-based)
- Files: `src/mcp/service.py`, `src/mcp/server.py`, `data/subscriptions.json` (gitignored)
- Tools: `hz_subscribe_topic`, `hz_list_subscriptions`
- Schedule execution: nothing yet, just persist
- **Gate**: Create + list subscription via MCP tool, file round-trips

#### Day 6: Three config packs
- Files: `config_packs/{ai-developers,livestream-compliance,overseas-policy}.json` + READMEs
- `horizon_adapter.load_config_pack(name)` helper
- **Gate**: For each pack, `hz_get_briefing(topic=<pack-default>, config_pack=<pack>)` returns ≥ 3 relevant items

#### Day 7: Week 1 closeout
- Run full test suite: `uv run pytest`
- Update `src/mcp/README.md` with new tools
- Record 1-minute demo gif of Claude Desktop calling `hz_get_briefing`
- Post Twitter + 小红书 build-in-public update
- **Gate**: demo gif posted publicly; all tests green

### Week 2 — Deploy, Billing, Launch

#### Day 8: HTTP transport + Fly.io
- Files: `src/mcp/server_http.py`, `fly.toml`, update `Dockerfile`
- `fly launch` → deploy to `horizon-mcp.fly.dev`
- **Gate**: External `curl https://horizon-mcp.fly.dev/healthz` returns 200

#### Day 9: Postgres migration
- Files: `src/storage/postgres.py` (new, implements RunStore interface)
- Env switch: `STORAGE_BACKEND=postgres|file`
- Apply Supabase migrations from §6.1
- **Gate**: One full run via MCP writes correctly to `runs` + `briefings` tables

#### Day 10: Auth + Quota
- Files: `src/mcp/middleware/{auth,quota}.py`, `src/api/{auth,me}.py` (FastAPI routes)
- Routes: `POST /auth/register`, `GET /me`
- Generate `sk_horizon_xxx` keys (32 hex chars + prefix)
- **Gate**: No key → 401; over-quota → 429

#### Day 11: Stripe + WeChat Pay
- Files: `src/api/billing/{stripe,wechatpay}.py`, webhook routes
- Stripe products + prices created in dashboard
- **Gate**: Test-mode Stripe checkout completes → tenant.plan updates to `pro`

#### Day 12: Landing page
- Update `docs/` GitHub Pages or create new `docs/commercial.md`
- Sections: hero, pricing, three config packs, demo, FAQ, signup CTA
- **Gate**: Lighthouse perf ≥ 90; 3-click path to checkout from homepage

#### Day 13: Distribution submissions
- PR to `modelcontextprotocol/servers`: `feat: add Horizon MCP — AI-curated news radar`
- Submit to Smithery (https://smithery.ai)
- Submit to mcp.run
- Post HN Show HN draft (do not post yet)
- **Gate**: All 3 submissions have public URLs

#### Day 14: Launch day
- Post Twitter long thread (10-12 tweets)
- Publish 小红书 carousel × 5
- Publish 公众号 long-form article (2000 chars)
- Post HN Show HN
- Post 即刻 + Reddit r/ClaudeAI + r/LocalLLaMA
- **Gate**: ≥ 1 real signup (even a friend) by end of Day 14

---

## 10. Risk Register

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| Upstream `Thysrael/Horizon` breaking change | Medium | Medium | Pin to a tested commit; subscribe to upstream releases; keep PR pipeline open |
| Anthropic launches official news MCP | Low | High | Vertical config packs and Chinese-localized pricing remain defensible |
| Qwen API price hike | Low | Medium | Multi-provider already supported, can swap to DeepSeek with one config change |
| Stripe / WeChat onboarding delay | Medium | Medium | Dual-rail; ship Stripe first; WeChat can come Day 16 if needed |
| Sprint slips past Day 14 | High | Low | Days 1-7 are blocking; Days 11 (billing) and 13 (distribution) can shift +1 week without killing launch |
| Cache layer correctness bugs | Medium | Low | Day 2 includes 3 unit tests minimum; default TTL conservative (60 min) |

---

## 11. Definition of Done

The sprint is complete when ALL of the following are true:

1. [ ] All 4 new tools live in production and callable from Claude Desktop with bearer token
2. [ ] Three config packs ship with READMEs and pass smoke tests
3. [ ] `topic_keywords` parameter integrated end-to-end
4. [ ] Postgres backend live with one tenant having completed runs
5. [ ] Stripe test-mode checkout works
6. [ ] WeChat Pay sandbox checkout works
7. [ ] Public landing page live with pricing
8. [ ] PR opened against `modelcontextprotocol/servers`
9. [ ] Launch posts published on Twitter, 小红书, HN, 公众号
10. [ ] At least one real user signs up (even unpaid)

---

## 12. Out of Scope (explicitly)

- ❌ Auto-publishing AI digests to 小红书 / Twitter matrix accounts (platform anti-AI policy)
- ❌ General news aggregation competing with TLDR / HN Daily
- ❌ Mobile app
- ❌ Self-trained models or fine-tuning
- ❌ SEO/GEO optimization for customer brands (Project C's territory)
- ❌ pgvector / semantic search (Phase 2)

---

## 13. Phase 2 Roadmap (Month 2-6)

- Vector RAG over `briefings_history` (pgvector)
- Custom private source UI for Pro users
- Team-tier multi-seat with shared config packs
- Auto-generated newsletter publishing (feeds Project G Path 1)
- Enterprise private deployment (sells via Project A Agent Outsourcing pipeline)

---

## 14. References

- Upstream: https://github.com/Thysrael/Horizon
- Existing MCP docs: `src/mcp/README.md`, `src/mcp/integration.md`
- Anthropic MCP servers: https://github.com/modelcontextprotocol/servers
- Smithery: https://smithery.ai
- Business companion doc: Obsidian `side-hustles/Project-G-Horizon情报引擎/04 - MCP 商业化 spec.md`

---

## 15. Companion Files

- `src/mcp/cache.py` (Day 2, new)
- `src/mcp/server_http.py` (Day 8, new)
- `src/mcp/middleware/auth.py` (Day 10, new)
- `src/mcp/middleware/quota.py` (Day 10, new)
- `src/storage/postgres.py` (Day 9, new)
- `src/scheduler/runner.py` (Day 5/10, new)
- `src/api/auth.py`, `src/api/me.py`, `src/api/billing/stripe.py`, `src/api/billing/wechatpay.py` (Days 10-11, new)
- `config_packs/*.json` (Day 6, new)
- `fly.toml` (Day 8, new)
- `Dockerfile` (Day 8, update)
- `pyproject.toml` (Day 8, add `horizon-mcp-http` script)
