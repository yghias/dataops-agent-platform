"""Documentation agent."""

from __future__ import annotations

from src.agents.base import BaseAgent
from src.common.contracts import AgentArtifact, TaskEnvelope


class DocumentationAgent(BaseAgent):
    name = "documentation_agent"

    def run(self, task: TaskEnvelope) -> AgentArtifact:
        return AgentArtifact(
            agent_name=self.name,
            artifact_type="operational_documentation",
            content=(
                "## Documentation Package\n"
                "- Capture purpose, dependencies, upstream contracts, and downstream consumers.\n"
                "- Include remediation steps, rollback, and approver ownership.\n"
                "- Link generated SQL assets to their operational runbook sections.\n"
            ),
            rationale="Documentation should be generated alongside operational artifacts so review packages are self-contained.",
            assumptions=["Documentation will be published with the approved artifact set."],
            warnings=["Review owner assignments before final publication."],
        )
