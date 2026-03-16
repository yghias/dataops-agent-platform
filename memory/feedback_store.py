"""Feedback storage for accepted and rejected artifacts."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path

from memory.decision_log import STORE_DIR


@dataclass
class FeedbackEvent:
    request_id: str
    artifact_type: str
    outcome: str
    comments: str
    score: int
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


class FeedbackStore:
    """Persists reviewer feedback for future analysis."""

    def __init__(self, path: Path | None = None) -> None:
        self.path = path or STORE_DIR / "feedback_store.jsonl"

    def append(self, event: FeedbackEvent) -> None:
        with self.path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(asdict(event)) + "\n")

    def recent(self, limit: int = 20) -> list[dict]:
        if not self.path.exists():
            return []
        with self.path.open("r", encoding="utf-8") as handle:
            rows = [json.loads(line) for line in handle if line.strip()]
        return rows[-limit:]
