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
