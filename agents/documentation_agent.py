"""Agent for technical documentation and runbooks."""

from __future__ import annotations

from agents.base_agent import AgentResult, BaseAgent, TaskRequest


class DocumentationAgent(BaseAgent):
    name = "documentation_agent"
    supported_domains = ("documentation", "runbook", "general")
    artifact_type = "technical_documentation"

    def run(self, task: TaskRequest) -> AgentResult:
        document = self.tools["doc_generator"].generate_runbook(
            title=task.context.get("title", "Data Asset Operational Runbook"),
            owner=task.context.get("owner", "data-platform"),
            system_name=task.context.get("system_name", "analytics_pipeline"),
            failure_modes=[
                "upstream source delivery missed SLA",
                "schema drift introduced an incompatible column",
                "warehouse load failed validation thresholds",
            ],
        )
        return AgentResult(
            agent_name=self.name,
            artifact_type=self.artifact_type,
            content=document,
            rationale="Documentation should be generated with operational sections that engineers can actually use during incidents.",
            assumptions=["Operators need ownership, diagnostics, rollback, and escalation details in one place."],
            warnings=["Review on-call routing and escalation expectations before publishing."],
        )
