"""Agent for data science workflow and feature design."""

from __future__ import annotations

from agents.base_agent import AgentResult, BaseAgent, TaskRequest


class DataScientistAgent(BaseAgent):
    name = "data_scientist_agent"
    supported_domains = ("ml", "data_science", "general")
    artifact_type = "feature_pipeline_design"

    def run(self, task: TaskRequest) -> AgentResult:
        content = (
            "## Feature Workflow Recommendation\n"
            "- Build features from contract-backed curated datasets rather than directly from raw ingestion tables.\n"
            "- Version feature logic and training datasets for reproducibility.\n"
            "- Separate offline training features from online serving constraints, but keep entity and timestamp semantics aligned.\n"
            "- Add data quality gates for null rates, leakage checks, and training-serving skew indicators.\n"
        )
        return AgentResult(
            agent_name=self.name,
            artifact_type=self.artifact_type,
            content=content,
            rationale="ML requests require reproducible feature generation and stronger validation around temporal correctness.",
            assumptions=["The platform will later integrate a feature store or model registry."],
            warnings=["Do not promote feature logic to production without validation against point-in-time correctness."],
        )
