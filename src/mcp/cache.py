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
