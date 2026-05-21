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
