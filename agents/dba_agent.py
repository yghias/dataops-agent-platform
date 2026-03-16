"""Agent for operational database safety and change review."""

from __future__ import annotations

from agents.base_agent import AgentResult, BaseAgent, TaskRequest


class DbaAgent(BaseAgent):
    name = "dba_agent"
    supported_domains = ("database", "operations", "general")
    artifact_type = "database_safety_review"

    def run(self, task: TaskRequest) -> AgentResult:
        content = (
            "## DBA Review Notes\n"
            "- Preserve read-only analysis until a reviewer approves execution.\n"
            "- Validate lock, concurrency, and rollback implications for any schema or index changes.\n"
            "- Require maintenance-window planning for material DDL in production environments.\n"
            "- Capture before/after performance evidence for optimization changes.\n"
        )
        return AgentResult(
            agent_name=self.name,
            artifact_type=self.artifact_type,
            content=content,
            rationale="Operational safety controls are required whenever the request could influence production database behavior.",
            assumptions=["The task may eventually feed a production change ticket or deployment workflow."],
            warnings=["No automated write activity should occur from this platform without approved execution."],
        )
