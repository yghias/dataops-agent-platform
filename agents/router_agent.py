"""Routing logic for task-to-agent assignment."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

from agents.base_agent import BaseAgent, TaskRequest


@dataclass
class RouteDecision:
    primary_agent: str
    supporting_agents: list[str]
    confidence: float
    reason: str


class RouterAgent:
    """Simple keyword and domain based router.

    In production, this would likely combine embeddings, policy context,
    prior task outcomes, and explicit role-aware routing rules.
    """

    def __init__(self, agents: Sequence[BaseAgent]) -> None:
        self.agents = {agent.name: agent for agent in agents}

    def route(self, task: TaskRequest) -> RouteDecision:
        prompt = task.prompt.lower()
        if any(word in prompt for word in ("dag", "airflow", "pipeline", "elt", "etl")):
            return RouteDecision(
                primary_agent="data_engineer_agent",
                supporting_agents=["observability_agent", "documentation_agent"],
                confidence=0.91,
                reason="Pipeline and orchestration keywords matched data engineering patterns.",
            )
        if any(word in prompt for word in ("schema", "model", "architecture", "grain")):
            return RouteDecision(
                primary_agent="data_architect_agent",
                supporting_agents=["database_engineer_agent", "dba_agent"],
                confidence=0.89,
                reason="Schema and modeling language indicates architecture review.",
            )
        if any(word in prompt for word in ("optimize", "query", "sql", "slow")):
            return RouteDecision(
                primary_agent="database_engineer_agent",
                supporting_agents=["dba_agent"],
                confidence=0.92,
                reason="SQL performance language indicates query engineering and DBA oversight.",
            )
        if any(word in prompt for word in ("metric", "kpi", "dashboard", "analysis")):
            return RouteDecision(
                primary_agent="data_analyst_agent",
                supporting_agents=["documentation_agent"],
                confidence=0.87,
                reason="Business metric language maps to analytics workflows.",
            )
        if any(word in prompt for word in ("feature", "model training", "experiment", "ml", "scoring")):
            return RouteDecision(
                primary_agent="data_scientist_agent",
                supporting_agents=["ai_ml_engineer_agent", "observability_agent"],
                confidence=0.86,
                reason="ML terminology indicates feature engineering and operationalization support.",
            )
        return RouteDecision(
            primary_agent="documentation_agent",
            supporting_agents=["observability_agent"],
            confidence=0.61,
            reason="Falling back to documentation-first triage because no stronger route matched.",
        )
