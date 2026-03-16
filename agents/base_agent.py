"""Shared contracts and base implementation for specialist agents."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


@dataclass
class TaskRequest:
    """Normalized task envelope used across the platform."""

    request_id: str
    requester_role: str
    prompt: str
    environment: str = "dev"
    domain: str = "general"
    risk_level: str = "medium"
    desired_artifact: str = "recommendation"
    context: dict[str, Any] = field(default_factory=dict)


@dataclass
class ToolEvidence:
    """Captured tool output summary referenced by an agent result."""

    tool_name: str
    summary: str
    payload: dict[str, Any] = field(default_factory=dict)


@dataclass
class AgentResult:
    """Structured output returned by every agent."""

    agent_name: str
    artifact_type: str
    content: str
    rationale: str
    assumptions: list[str]
    warnings: list[str]
    evidence: list[ToolEvidence] = field(default_factory=list)
    recommended_next_step: str = "submit_for_review"
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


class BaseAgent:
    """Base class for all platform agents.

    Agents are expected to produce draft artifacts, not final production actions.
    """

    name = "base_agent"
    supported_domains: tuple[str, ...] = ("general",)
    artifact_type = "recommendation"

    def __init__(self, tools: dict[str, Any] | None = None) -> None:
        self.tools = tools or {}

    def can_handle(self, task: TaskRequest) -> bool:
        return task.domain in self.supported_domains or "general" in self.supported_domains

    def describe_scope(self) -> str:
        return (
            f"{self.name} handles domains {', '.join(self.supported_domains)} "
            f"and produces {self.artifact_type} artifacts."
        )

    def build_prompt(self, task: TaskRequest) -> str:
        context_lines = "\n".join(f"- {key}: {value}" for key, value in sorted(task.context.items()))
        return (
            f"Role: {self.name}\n"
            f"Environment: {task.environment}\n"
            f"Risk: {task.risk_level}\n"
            f"Requested artifact: {task.desired_artifact}\n"
            f"Task: {task.prompt}\n"
            f"Context:\n{context_lines or '- none provided'}"
        )

    def run(self, task: TaskRequest) -> AgentResult:
        raise NotImplementedError("Agents must implement run().")
