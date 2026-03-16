"""Prompt version registry."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path

from memory.decision_log import STORE_DIR


@dataclass
class PromptVersion:
    agent_name: str
    version: str
    prompt_template: str
    notes: str
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


class PromptRegistry:
    """Stores prompt templates used by agents and workflows."""

    def __init__(self, path: Path | None = None) -> None:
        self.path = path or STORE_DIR / "prompt_registry.jsonl"

    def register(self, prompt: PromptVersion) -> None:
        with self.path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(asdict(prompt)) + "\n")

    def latest_for_agent(self, agent_name: str) -> dict | None:
        if not self.path.exists():
            return None
        with self.path.open("r", encoding="utf-8") as handle:
            matches = [json.loads(line) for line in handle if f'"agent_name": "{agent_name}"' in line]
        return matches[-1] if matches else None
