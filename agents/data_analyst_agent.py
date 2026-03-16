"""Agent for KPI and semantic metric definition."""

from __future__ import annotations

from agents.base_agent import AgentResult, BaseAgent, TaskRequest, ToolEvidence


class DataAnalystAgent(BaseAgent):
    name = "data_analyst_agent"
    supported_domains = ("analytics", "metrics", "general")
    artifact_type = "metric_definition"

    def run(self, task: TaskRequest) -> AgentResult:
        metric_name = task.context.get("metric_name", "monthly_active_customers")
        metadata = self.tools["metadata"].read_metric(metric_name)
        sql = (
            "select\n"
            "    date_trunc('month', activity_date) as activity_month,\n"
            "    count(distinct customer_id) as monthly_active_customers\n"
            "from analytics.customer_activity\n"
            "where activity_flag = true\n"
            "group by 1"
        )
        content = (
            f"## KPI Definition: `{metric_name}`\n"
            "- Grain: calendar month\n"
            "- Entity: unique active customer\n"
            "- Inclusion rule: customer must have at least one qualifying activity during the month\n"
            "- Publication layer: analytics mart backed by Snowflake SQL\n\n"
            f"```sql\n{sql}\n```\n"
        )
        return AgentResult(
            agent_name=self.name,
            artifact_type=self.artifact_type,
            content=content,
            rationale="Metric requests need business-grain clarity and stable SQL semantics before downstream dashboard use.",
            assumptions=["Activity definitions are stable and recorded in a canonical fact table."],
            warnings=["Business owner review is required before adopting this metric as a canonical KPI."],
            evidence=[ToolEvidence("metadata_reader", "Looked up any prior metric definition metadata.", metadata)],
        )
