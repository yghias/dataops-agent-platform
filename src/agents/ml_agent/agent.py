"""AI/ML engineer agent."""

from __future__ import annotations

from src.agents.base import BaseAgent
from src.common.contracts import AgentArtifact, TaskEnvelope


class MlEngineerAgent(BaseAgent):
    name = "ai_ml_engineer_agent"

    def run(self, task: TaskEnvelope) -> AgentArtifact:
        return AgentArtifact(
            agent_name=self.name,
            artifact_type="ml_pipeline_guidance",
            content=(
                "## Model Pipeline Guidance\n"
                "- Use batch feature generation in Snowflake and persist training snapshots by version.\n"
                "- Keep retrieval corpora and evaluation sets under explicit version control.\n"
                "- Package model approval separately from data contract approval.\n"
            ),
            rationale="ML pipeline recommendations should preserve dataset reproducibility and evaluation traceability.",
            assumptions=["Model-serving and retrieval assets are approved through the same review workflow."],
            warnings=["Do not promote retraining jobs without reviewer sign-off and evaluation evidence."],
        )
