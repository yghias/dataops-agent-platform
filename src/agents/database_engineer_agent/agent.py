"""Database engineer agent."""

from __future__ import annotations

from src.agents.base import BaseAgent
from src.common.contracts import AgentArtifact, EvidenceRecord, TaskEnvelope


class DatabaseEngineerAgent(BaseAgent):
    name = "database_engineer_agent"

    def run(self, task: TaskEnvelope) -> AgentArtifact:
        analysis = self.tools["query_optimizer"].analyze(task.payload.get("sql_text", "select * from marts.pipeline_health_mart"))
        return AgentArtifact(
            agent_name=self.name,
            artifact_type="query_optimization",
            content=(
                "## Query Review\n"
                "- Prefer explicit column projection for repeated reporting queries.\n"
                "- Push date predicates into base tables and incremental models.\n"
                "- Validate clustering choice against bytes scanned and execution history.\n"
            ),
            rationale="Database engineering tasks should interpret SQL performance through Snowflake execution behavior.",
            assumptions=["The target query operates on large operational telemetry tables."],
            warnings=["Apply clustering changes only after runtime validation in non-production."],
            evidence=[EvidenceRecord("query_optimizer", "Generated query optimization notes.", analysis)],
        )
