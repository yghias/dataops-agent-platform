"""Data scientist agent."""

from __future__ import annotations

from src.agents.base import BaseAgent
from src.common.contracts import AgentArtifact, TaskEnvelope


class DataScientistAgent(BaseAgent):
    name = "data_scientist_agent"

    def run(self, task: TaskEnvelope) -> AgentArtifact:
        return AgentArtifact(
            agent_name=self.name,
            artifact_type="feature_dataset_design",
            content=(
                "## Feature Dataset Preparation\n"
                "- Join pipeline health, data quality, and query performance marts by day and environment.\n"
                "- Label historical failures using pipeline run outcomes.\n"
                "- Exclude post-failure leakage columns from training data.\n"
            ),
            rationale="Feature generation should be based on curated operational marts and reproducible SQL extracts.",
            assumptions=["Historical run outcomes are retained in platform metadata tables."],
            warnings=["Validate feature leakage before model training."],
        )
