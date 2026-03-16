"""Artifact validation and scoring helpers."""

from __future__ import annotations

from agents.base_agent import AgentResult


class QualityChecker:
    """Scores generated artifacts and recommends baseline controls."""

    def recommend_checks(self, asset_type: str) -> dict:
        return {
            "asset_type": asset_type,
            "checks": [
                "freshness",
                "row_count_change",
                "null_rate",
                "schema_drift",
            ],
        }

    def score_result(self, result: AgentResult) -> dict:
        score = 80
        if result.assumptions:
            score += 5
        if result.warnings:
            score -= min(len(result.warnings) * 3, 12)
        if "##" in result.content:
            score += 5
        return {
            "agent_name": result.agent_name,
            "artifact_type": result.artifact_type,
            "score": max(min(score, 100), 0),
            "warnings": result.warnings,
        }
