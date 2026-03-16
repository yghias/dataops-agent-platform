"""Agent for SQL and physical design optimization."""

from __future__ import annotations

from agents.base_agent import AgentResult, BaseAgent, TaskRequest, ToolEvidence


class DatabaseEngineerAgent(BaseAgent):
    name = "database_engineer_agent"
    supported_domains = ("sql", "database", "general")
    artifact_type = "query_optimization"

    def run(self, task: TaskRequest) -> AgentResult:
        sql_text = task.context.get(
            "sql",
            "select * from analytics.orders o join analytics.customers c on o.customer_id = c.customer_id",
        )
        findings = self.tools["query_optimizer"].analyze(sql_text)
        schema = self.tools["schema"].inspect_table(task.context.get("table", "analytics.orders"))
        content = (
            "## Query Optimization Review\n"
            f"- Optimization score: {findings['score']}/100\n"
            "- Prefer explicit column lists over `select *` for stable performance and lineage clarity.\n"
            "- Confirm predicate selectivity and partition pruning on large fact tables.\n"
            "- Review join keys and supporting indexes or clustering strategy.\n"
        )
        warnings = findings["warnings"] or ["No critical issues detected by heuristic review."]
        return AgentResult(
            agent_name=self.name,
            artifact_type=self.artifact_type,
            content=content,
            rationale="The request maps to query-shape review plus physical storage considerations.",
            assumptions=["The warehouse workload includes large scans where projection and pruning matter."],
            warnings=warnings,
            evidence=[
                ToolEvidence("query_optimizer", "Ran heuristic SQL review.", findings),
                ToolEvidence("schema_inspector", "Loaded table metadata for optimization context.", schema),
            ],
        )
