"""Agent for ML engineering and model operationalization."""

from __future__ import annotations

from agents.base_agent import AgentResult, BaseAgent, TaskRequest


class AiMlEngineerAgent(BaseAgent):
    name = "ai_ml_engineer_agent"
    supported_domains = ("ml", "platform", "general")
    artifact_type = "ml_operationalization_guidance"

    def run(self, task: TaskRequest) -> AgentResult:
        content = (
            "## ML Operationalization Guidance\n"
            "- Package training, evaluation, and scoring as separate workflow stages with clear promotion gates.\n"
            "- Track dataset, feature logic, and model version together for rollback safety.\n"
            "- Require review before activating automated scoring or retraining schedules.\n"
            "- Emit model and data quality telemetry into the same observability layer used by the data platform.\n"
        )
        return AgentResult(
            agent_name=self.name,
            artifact_type=self.artifact_type,
            content=content,
            rationale="ML systems need stronger deployment, versioning, and monitoring controls than a one-shot modeling notebook workflow.",
            assumptions=["The team expects to transition experimental models into repeatable production workflows."],
            warnings=["Human approval should be required before model promotion and scheduled retraining."],
        )
