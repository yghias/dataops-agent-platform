"""Cloud data platform agent."""

from __future__ import annotations

from src.agents.base import BaseAgent
from src.common.contracts import AgentArtifact, TaskEnvelope


class CloudDataPlatformAgent(BaseAgent):
    name = "cloud_data_platform_agent"

    def run(self, task: TaskEnvelope) -> AgentArtifact:
        return AgentArtifact(
            agent_name=self.name,
            artifact_type="platform_guidance",
            content=(
                "## Cloud Data Platform Guidance\n"
                "- Use separate Snowflake warehouses for ingestion, transforms, and diagnostics.\n"
                "- Store landed files in S3 with partition-aware paths.\n"
                "- Keep Airflow worker environment separate from warehouse execution credentials.\n"
            ),
            rationale="Cloud guidance should focus on environment isolation and cost-aware compute planning.",
            assumptions=["AWS is the primary runtime environment."],
            warnings=["Warehouse sizing recommendations should be validated against real query history."],
        )
