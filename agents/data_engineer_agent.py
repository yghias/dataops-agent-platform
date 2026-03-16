"""Agent for ETL, ELT, and data pipeline generation."""

from __future__ import annotations

from agents.base_agent import AgentResult, BaseAgent, TaskRequest, ToolEvidence


class DataEngineerAgent(BaseAgent):
    name = "data_engineer_agent"
    supported_domains = ("data_engineering", "general")
    artifact_type = "pipeline_design"

    def run(self, task: TaskRequest) -> AgentResult:
        lineage = self.tools["lineage"].get_lineage(task.context.get("asset", "stg_orders"))
        quality_plan = self.tools["quality"].recommend_checks("pipeline")
        dag = self.tools["dag_generator"].generate(
            dag_id=task.context.get("dag_id", "daily_orders_ingestion"),
            schedule=task.context.get("schedule", "0 5 * * *"),
            source_system=task.context.get("source_system", "crm"),
            target_table=task.context.get("target_table", "analytics.orders"),
        )
        content = (
            "## Proposed Pipeline Design\n"
            "- Land source extracts into a raw zone partitioned by load date.\n"
            "- Apply idempotent staging logic with watermark-based incremental ingestion.\n"
            "- Publish curated warehouse models with test coverage before downstream exposure.\n\n"
            "## Orchestration Draft\n"
            f"```python\n{dag}\n```\n"
        )
        return AgentResult(
            agent_name=self.name,
            artifact_type=self.artifact_type,
            content=content,
            rationale="The request maps to a standard ingestion-to-curated pattern with orchestration and quality controls.",
            assumptions=[
                "Source extracts are available on a predictable schedule.",
                "Target warehouse supports partition pruning or clustering.",
            ],
            warnings=["Execution is not authorized until a human reviewer approves the generated design and DAG."],
            evidence=[
                ToolEvidence("lineage_tool", "Checked upstream/downstream dependency expectations.", lineage),
                ToolEvidence("quality_checker", "Suggested baseline pipeline quality controls.", quality_plan),
            ],
        )
