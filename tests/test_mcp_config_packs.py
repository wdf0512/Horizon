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
