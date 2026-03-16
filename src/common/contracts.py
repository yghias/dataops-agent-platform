"""Shared task and result contracts for the src-based runtime."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


@dataclass
class TaskEnvelope:
    task_id: str
    requester_role: str
    request_type: str
    prompt: str
    environment: str
    payload: dict[str, Any] = field(default_factory=dict)
    approval_required: bool = True


@dataclass
class EvidenceRecord:
    tool_name: str
    summary: str
    payload: dict[str, Any] = field(default_factory=dict)


@dataclass
class AgentArtifact:
    agent_name: str
    artifact_type: str
    content: str
    rationale: str
    assumptions: list[str]
    warnings: list[str]
    evidence: list[EvidenceRecord] = field(default_factory=list)
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
