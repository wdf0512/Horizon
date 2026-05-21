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
