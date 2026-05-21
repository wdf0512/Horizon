"""MCP-server pydantic models."""
from __future__ import annotations

from datetime import datetime, timezone
from typing import List, Optional

from pydantic import BaseModel, Field


class Subscription(BaseModel):
    id: str
    topic: str
    schedule: str
    channels: List[str]
    config_pack: Optional[str] = None
    active: bool = True
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    last_run_at: Optional[datetime] = None
