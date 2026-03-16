"""Execution event helpers."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass
class ExecutionEvent:
    execution_event_id: str
    task_id: str
    recommendation_id: str
    execution_status: str
    executed_by: str
    executed_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
