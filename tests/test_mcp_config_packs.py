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
    assert captured_kwargs["threshold"] == 7.0
