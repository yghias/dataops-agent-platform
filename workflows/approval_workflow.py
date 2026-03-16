"""Human approval and review packaging workflow."""

from __future__ import annotations

from dataclasses import asdict
from typing import Any

from agents.base_agent import AgentResult, TaskRequest
from agents.router_agent import RouteDecision
from memory.decision_log import DecisionLog, HumanDecision
from tools.quality_checker import QualityChecker


class ApprovalWorkflow:
    """Packages drafts for review and records human decisions."""

    def __init__(self) -> None:
        self.quality_checker = QualityChecker()
        self.decision_log = DecisionLog()

    def package_for_review(
        self,
        task: TaskRequest,
        route: RouteDecision,
        results: list[AgentResult],
    ) -> dict[str, Any]:
        quality = [self.quality_checker.score_result(result) for result in results]
        return {
            "request_id": task.request_id,
            "route_reason": route.reason,
            "review_required": True,
            "primary_agent": route.primary_agent,
            "supporting_agents": route.supporting_agents,
            "quality_scores": quality,
            "artifacts": [asdict(result) for result in results],
            "recommended_action": "approve_or_request_changes",
        }

    def record_decision(
        self,
        request_id: str,
        reviewer: str,
        decision: str,
        rationale: str,
        artifact_refs: list[str],
    ) -> HumanDecision:
        human_decision = HumanDecision(
            request_id=request_id,
            reviewer=reviewer,
            decision=decision,
            rationale=rationale,
            artifact_refs=artifact_refs,
        )
        self.decision_log.append(human_decision)
        return human_decision
