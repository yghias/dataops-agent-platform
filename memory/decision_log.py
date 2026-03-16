"""Decision logging for human approvals and rejections."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path


STORE_DIR = Path("memory/store")
STORE_DIR.mkdir(parents=True, exist_ok=True)


@dataclass
class HumanDecision:
    request_id: str
    reviewer: str
    decision: str
    rationale: str
    artifact_refs: list[str]
    decided_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


class DecisionLog:
    """Appends immutable human decisions to a JSONL file."""

    def __init__(self, path: Path | None = None) -> None:
        self.path = path or STORE_DIR / "decision_log.jsonl"

    def append(self, decision: HumanDecision) -> None:
        with self.path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(asdict(decision)) + "\n")

    def read_all(self) -> list[dict]:
        if not self.path.exists():
            return []
        with self.path.open("r", encoding="utf-8") as handle:
            return [json.loads(line) for line in handle if line.strip()]
