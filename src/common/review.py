"""Human review packet helpers."""

from __future__ import annotations

from dataclasses import asdict

from src.common.contracts import AgentArtifact, TaskEnvelope


def build_review_packet(task: TaskEnvelope, artifacts: list[AgentArtifact], route_reason: str) -> dict:
    return {
        "task_id": task.task_id,
        "request_type": task.request_type,
        "environment": task.environment,
        "approval_required": task.approval_required,
        "route_reason": route_reason,
        "artifacts": [asdict(artifact) for artifact in artifacts],
        "review_status": "pending_human_review",
    }
