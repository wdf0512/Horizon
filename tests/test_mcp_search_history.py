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
