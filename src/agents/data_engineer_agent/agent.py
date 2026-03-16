"""Data engineer agent."""

from __future__ import annotations

from src.agents.base import BaseAgent
from src.common.contracts import AgentArtifact, EvidenceRecord, TaskEnvelope


class DataEngineerAgent(BaseAgent):
    name = "data_engineer_agent"

    def run(self, task: TaskEnvelope) -> AgentArtifact:
        model = self.tools["dbt_generator"].generate_model("stg_pipeline_runs", "raw", "pipeline_runs")
        dag_text = self.tools["pipeline_diagnostics"].render_dag_summary(task.payload.get("dag_id", "platform_metadata_ingestion"))
        return AgentArtifact(
            agent_name=self.name,
            artifact_type="pipeline_package",
            content=(
                "## Snowflake Transformation\n"
                f"```sql\n{model['sql']}\n```\n\n"
                "## Airflow Control Notes\n"
                f"{dag_text}\n"
            ),
            rationale="Pipeline generation requests should emit SQL-first transformation assets and orchestration notes.",
            assumptions=["Source ingestion lands successfully into raw zone tables."],
            warnings=["Publish to production only after contract validation and human approval."],
            evidence=[EvidenceRecord("dbt_generator", "Generated incremental model scaffold.", model)],
        )
