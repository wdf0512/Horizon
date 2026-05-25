from __future__ import annotations

import time

from src.mcp.cache import BriefingCache, CacheKey


def test_cache_hit_within_ttl():
    cache = BriefingCache(max_entries=8, default_ttl_seconds=60, now=lambda: 1_000)
    key = CacheKey(tenant_id="default", topic="llm", language="zh",
                   hours=24, min_score=7.0, config_pack=None)
    cache.set(key, {"foo": "bar"})
    cache.now = lambda: 1_030
    assert cache.get(key) == {"foo": "bar"}


def test_cache_miss_after_ttl():
    cache = BriefingCache(max_entries=8, default_ttl_seconds=60, now=lambda: 1_000)
    key = CacheKey(tenant_id="default", topic="llm", language="zh",
                   hours=24, min_score=7.0, config_pack=None)
    cache.set(key, {"foo": "bar"})
    cache.now = lambda: 1_061
    assert cache.get(key) is None


def test_cache_miss_on_different_key():
    cache = BriefingCache(max_entries=8, default_ttl_seconds=60, now=lambda: 1_000)
    a = CacheKey(tenant_id="default", topic="llm", language="zh",
                 hours=24, min_score=7.0, config_pack=None)
    b = CacheKey(tenant_id="default", topic="llm", language="en",
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
    cache.set(k("c"), 3)   # should evict 'b'
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

    fixed_now[0] = 1_030.0
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
