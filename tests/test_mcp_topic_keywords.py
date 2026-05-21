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
