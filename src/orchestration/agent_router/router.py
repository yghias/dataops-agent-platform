"""Deterministic task routing."""

from __future__ import annotations

from dataclasses import dataclass

from src.common.contracts import TaskEnvelope


@dataclass
class RouteDecision:
    primary_agent: str
    supporting_agents: list[str]
    reason: str


class AgentRouter:
    def route(self, task: TaskEnvelope) -> RouteDecision:
        prompt = task.prompt.lower()
        if any(token in prompt for token in ("query", "optimize", "slow")):
            return RouteDecision("database_engineer_agent", ["dba_agent"], "Query optimization request.")
        if any(token in prompt for token in ("pipeline", "airflow", "dbt", "transformation")):
            return RouteDecision("data_engineer_agent", ["cloud_data_platform_agent"], "Pipeline and SQL transformation request.")
        if any(token in prompt for token in ("schema", "contract", "model")):
            return RouteDecision("data_architect_agent", ["dba_agent"], "Schema or contract review request.")
        if any(token in prompt for token in ("metric", "kpi", "semantic")):
            return RouteDecision("data_analyst_agent", [], "Semantic metric request.")
        if any(token in prompt for token in ("feature", "experiment")):
            return RouteDecision("data_scientist_agent", ["ai_ml_engineer_agent"], "Feature generation request.")
        if any(token in prompt for token in ("rag", "evaluation", "model pipeline")):
            return RouteDecision("ai_ml_engineer_agent", [], "AI/ML platform request.")
        if any(token in prompt for token in ("failure", "anomaly", "debug")):
            return RouteDecision("observability_agent", ["data_engineer_agent"], "Incident and observability request.")
        return RouteDecision("documentation_agent", [], "Default routing for documentation and review packaging.")
