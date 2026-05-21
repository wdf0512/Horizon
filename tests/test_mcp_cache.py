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
