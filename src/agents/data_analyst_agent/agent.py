"""Data analyst agent."""

from __future__ import annotations

from src.agents.base import BaseAgent
from src.common.contracts import AgentArtifact, TaskEnvelope


class DataAnalystAgent(BaseAgent):
    name = "data_analyst_agent"

    def run(self, task: TaskEnvelope) -> AgentArtifact:
        return AgentArtifact(
            agent_name=self.name,
            artifact_type="semantic_metric",
            content=(
                "## KPI Definition\n"
                "```sql\n"
                "select\n"
                "    pipeline_id,\n"
                "    round(count_if(status = 'success') / nullif(count(*), 0), 4) as pipeline_success_rate\n"
                "from platform.pipeline_runs\n"
                "group by 1\n"
                "```\n"
            ),
            rationale="Metric generation should publish reusable SQL definitions rather than embed business logic in Python.",
            assumptions=["Pipeline status values are standardized to success/failed/running."],
            warnings=["Canonical metrics require review before dashboard publication."],
        )
