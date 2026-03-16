"""Observability agent."""

from __future__ import annotations

from src.agents.base import BaseAgent
from src.common.contracts import AgentArtifact, TaskEnvelope


class ObservabilityAgent(BaseAgent):
    name = "observability_agent"

    def run(self, task: TaskEnvelope) -> AgentArtifact:
        return AgentArtifact(
            agent_name=self.name,
            artifact_type="incident_analysis",
            content=(
                "## Observability Analysis\n"
                "- Review freshness lag, failed task count, and quality check failures together.\n"
                "- Compare current failure patterns against trailing 7-day averages.\n"
                "- Escalate schema drift incidents before rerunning publication tasks.\n"
            ),
            rationale="Failure analysis should combine orchestration, contract, and warehouse signals in one review package.",
            assumptions=["Airflow metadata and quality results are available for the failing run."],
            warnings=["Do not rerun downstream publish tasks until upstream data quality checks pass."],
        )
