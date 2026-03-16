"""Data architect agent."""

from __future__ import annotations

from src.agents.base import BaseAgent
from src.common.contracts import AgentArtifact, EvidenceRecord, TaskEnvelope


class DataArchitectAgent(BaseAgent):
    name = "data_architect_agent"

    def run(self, task: TaskEnvelope) -> AgentArtifact:
        schema = self.tools["schema_inspector"].inspect_table(task.payload.get("table_name", "platform.data_assets"))
        return AgentArtifact(
            agent_name=self.name,
            artifact_type="schema_review",
            content=(
                "## Canonical Model Review\n"
                "- Preserve domain ownership on `data_assets` and `table_lineage` separately.\n"
                "- Keep operational telemetry and business-facing marts in different schemas.\n"
                "- Use contract-backed staging models before canonical mart publication.\n"
            ),
            rationale="Schema review should focus on grain, ownership, and long-term change resilience.",
            assumptions=["Platform metadata and operational telemetry have different retention profiles."],
            warnings=["Schema changes require downstream lineage review before approval."],
            evidence=[EvidenceRecord("schema_inspector", "Loaded current warehouse metadata.", schema)],
        )
