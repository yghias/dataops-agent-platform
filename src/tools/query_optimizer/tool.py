"""Query optimization helper."""

from __future__ import annotations


class QueryOptimizer:
    def analyze(self, sql_text: str) -> dict:
        recommendations: list[str] = []
        score = 100
        lowered = sql_text.lower()
        if "select *" in lowered:
            score -= 20
            recommendations.append("Replace select * with explicit projection.")
        if "count(distinct" in lowered:
            recommendations.append("Consider whether a pre-aggregated mart can reduce repeated distinct counting.")
        if "where" not in lowered:
            score -= 10
            recommendations.append("Add bounded predicates for large Snowflake tables where practical.")
        if not recommendations:
            recommendations.append("Validate query plan against clustering and bytes scanned.")
        return {"score": score, "recommendations": recommendations}
