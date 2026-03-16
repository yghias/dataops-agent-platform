"""Agent for observability and data quality controls."""

from __future__ import annotations

from agents.base_agent import AgentResult, BaseAgent, TaskRequest, ToolEvidence


class ObservabilityAgent(BaseAgent):
    name = "observability_agent"
    supported_domains = ("observability", "quality", "general")
    artifact_type = "observability_plan"

    def run(self, task: TaskRequest) -> AgentResult:
        checks = self.tools["quality"].recommend_checks(task.context.get("asset_type", "table"))
        content = (
            "## Observability Plan\n"
            "- Add freshness, row-count, null-rate, and distribution checks.\n"
            "- Emit pipeline-level runtime metrics and SLA adherence signals.\n"
            "- Capture lineage-aware alert routing to prioritize high-blast-radius failures.\n"
            "- Store validation evidence alongside the generated artifact.\n"
        )
        return AgentResult(
            agent_name=self.name,
            artifact_type=self.artifact_type,
            content=content,
            rationale="Generated data assets need quality and operability controls as part of the initial draft, not as an afterthought.",
            assumptions=["The target environment supports structured logging and alert integrations."],
            warnings=["Thresholds should be reviewed by domain owners before activation."],
            evidence=[ToolEvidence("quality_checker", "Generated suggested validation controls.", checks)],
        )
