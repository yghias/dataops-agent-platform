"""Agent for platform and CI/CD guidance."""

from __future__ import annotations

from agents.base_agent import AgentResult, BaseAgent, TaskRequest


class CloudPlatformAgent(BaseAgent):
    name = "cloud_platform_agent"
    supported_domains = ("platform", "cloud", "general")
    artifact_type = "platform_guidance"

    def run(self, task: TaskRequest) -> AgentResult:
        content = (
            "## Platform Guidance\n"
            "- Use protected environments for staging and production deployments.\n"
            "- Gate release promotion on lint, unit tests, artifact validation, and approver sign-off.\n"
            "- Route secrets through a vault-backed mechanism rather than environment literals in pipeline code.\n"
            "- Separate generation jobs from deployment jobs to preserve review boundaries.\n"
        )
        return AgentResult(
            agent_name=self.name,
            artifact_type=self.artifact_type,
            content=content,
            rationale="The request requires infrastructure and delivery guidance aligned to controlled change management.",
            assumptions=["The team uses GitHub Actions or a similar workflow engine for CI/CD."],
            warnings=["Do not allow AI-generated infrastructure changes to auto-apply without human review."],
        )
