"""DBA agent."""

from __future__ import annotations

from src.agents.base import BaseAgent
from src.common.contracts import AgentArtifact, TaskEnvelope


class DbaAgent(BaseAgent):
    name = "dba_agent"

    def run(self, task: TaskEnvelope) -> AgentArtifact:
        return AgentArtifact(
            agent_name=self.name,
            artifact_type="database_operations_review",
            content=(
                "## DBA Review\n"
                "- Confirm warehouse role and schema access before execution.\n"
                "- Capture rollback steps for DDL-affecting changes.\n"
                "- Prefer non-peak windows for storage or clustering changes.\n"
            ),
            rationale="DBA review is required for production-safety and maintenance controls.",
            assumptions=["Task may affect high-volume Snowflake objects."],
            warnings=["Do not execute write-affecting SQL without explicit approval."],
        )
