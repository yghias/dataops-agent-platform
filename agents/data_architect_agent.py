"""Agent for schema and platform architecture review."""

from __future__ import annotations

from agents.base_agent import AgentResult, BaseAgent, TaskRequest, ToolEvidence


class DataArchitectAgent(BaseAgent):
    name = "data_architect_agent"
    supported_domains = ("architecture", "modeling", "general")
    artifact_type = "architecture_review"

    def run(self, task: TaskRequest) -> AgentResult:
        table_name = task.context.get("table", "analytics.customer_360")
        schema = self.tools["schema"].inspect_table(table_name)
        metadata = self.tools["metadata"].read_asset(table_name)
        content = (
            f"## Architecture Review for `{table_name}`\n"
            "- Confirm business grain at the customer-account relationship level.\n"
            "- Separate mutable profile attributes from event history to avoid mixed-grain semantics.\n"
            "- Publish contract-backed dimensions and facts rather than embedding all use cases into one denormalized table.\n"
            "- Add ownership and SLA metadata before production adoption.\n"
        )
        return AgentResult(
            agent_name=self.name,
            artifact_type=self.artifact_type,
            content=content,
            rationale="The request benefits from an explicit review of grain, ownership, extensibility, and downstream analytics ergonomics.",
            assumptions=["The proposed schema is intended for both analytics and operational reporting use cases."],
            warnings=["Review key design and slowly changing attribute strategy with the data engineering and analytics owners."],
            evidence=[
                ToolEvidence("schema_inspector", "Inspected representative schema metadata.", schema),
                ToolEvidence("metadata_reader", "Retrieved ownership and SLA posture.", metadata),
            ],
        )
