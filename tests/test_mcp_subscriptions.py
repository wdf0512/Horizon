from __future__ import annotations

from pathlib import Path

from src.mcp.subscriptions_store import SubscriptionStore
from src.mcp.models import Subscription


def test_store_create_and_list(tmp_path: Path):
    store = SubscriptionStore(tmp_path / "subs.json")
    sub = store.create(
        topic="AI inference",
        schedule="0 9 * * *",
        channels=["webhook"],
        config_pack=None,
    )
    assert isinstance(sub, Subscription)
    assert sub.topic == "AI inference"
    assert sub.active is True
    assert sub.id

    listed = store.list()
    assert len(listed) == 1
    assert listed[0].id == sub.id


def test_store_create_is_idempotent_on_topic(tmp_path: Path):
    store = SubscriptionStore(tmp_path / "subs.json")
    a = store.create(topic="AI", schedule="0 9 * * *", channels=["webhook"])
    b = store.create(topic="AI", schedule="0 10 * * *", channels=["webhook"])
    assert a.id == b.id
    assert b.schedule == "0 10 * * *"
    assert len(store.list()) == 1


def test_store_delete_returns_true_for_existing(tmp_path: Path):
    store = SubscriptionStore(tmp_path / "subs.json")
    sub = store.create(topic="A", schedule="0 9 * * *", channels=["webhook"])
    assert store.delete(sub.id) is True
    assert store.list() == []


def test_store_delete_returns_false_for_missing(tmp_path: Path):
    store = SubscriptionStore(tmp_path / "subs.json")
    assert store.delete("nope") is False


def test_store_round_trips_through_file(tmp_path: Path):
    path = tmp_path / "subs.json"
    a = SubscriptionStore(path)
    a.create(topic="X", schedule="0 9 * * *", channels=["webhook"])

    b = SubscriptionStore(path)
    listed = b.list()
    assert len(listed) == 1
    assert listed[0].topic == "X"


import asyncio
from src.mcp.service import HorizonPipelineService


def test_service_subscribe_round_trip(tmp_path):
    service = HorizonPipelineService(runs_root=tmp_path / "mcp-runs")
    service.subscriptions_path = tmp_path / "subs.json"
    service._subscription_store = None

    created = asyncio.run(service.subscribe_topic(
        topic="LLM inference",
        schedule="0 9 * * *",
        channels=["webhook"],
    ))
    assert created["topic"] == "LLM inference"

    listed = asyncio.run(service.list_subscriptions())
    assert listed["count"] == 1

    deleted = asyncio.run(service.delete_subscription(created["id"]))
    assert deleted["deleted"] is True

    listed2 = asyncio.run(service.list_subscriptions())
    assert listed2["count"] == 0


def test_hz_subscribe_topic_tool_envelope(tmp_path, monkeypatch):
    from src.mcp import server
    monkeypatch.setattr(server.service, "subscriptions_path", tmp_path / "subs.json")
    monkeypatch.setattr(server.service, "_subscription_store", None)

    result = asyncio.run(server.hz_subscribe_topic(
        topic="X", schedule="0 9 * * *", channels=["webhook"],
    ))
    assert result["ok"] is True
    assert result["tool"] == "hz_subscribe_topic"
    assert result["data"]["topic"] == "X"
