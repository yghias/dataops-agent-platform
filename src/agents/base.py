"""Base agent implementation."""

from __future__ import annotations

from typing import Any

from src.common.contracts import AgentArtifact, TaskEnvelope


class BaseAgent:
    name = "base_agent"

    def __init__(self, tools: dict[str, Any] | None = None) -> None:
        self.tools = tools or {}

    def run(self, task: TaskEnvelope) -> AgentArtifact:
        raise NotImplementedError
