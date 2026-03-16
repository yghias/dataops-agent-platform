"""Heuristic Snowflake SQL optimization tool."""

from __future__ import annotations

import re


class QueryOptimizer:
    """Analyzes SQL text and returns practical tuning recommendations."""

    def analyze(self, sql_text: str) -> dict:
        score = 100
        warnings: list[str] = []
        recommendations: list[str] = []
        lowered = sql_text.lower()

        if "select *" in lowered:
            score -= 20
            warnings.append("Query uses `select *`, which can increase scan cost and destabilize downstream contracts.")
            recommendations.append("Project only the columns required by the consuming use case.")
        if "qualify" not in lowered and "row_number(" in lowered:
            recommendations.append("For Snowflake window-filter patterns, consider `QUALIFY` to keep row filtering close to the window definition.")
        if " join " in lowered and " on " not in lowered:
            score -= 35
            warnings.append("Join detected without an explicit join condition.")
            recommendations.append("Add explicit join predicates and validate cardinality expectations.")
        if re.search(r"where\s+1\s*=\s*1", lowered):
            score -= 5
            recommendations.append("Remove scaffolding predicates before production use.")
        if "date_trunc" not in lowered and "group by" in lowered:
            recommendations.append("Confirm aggregation grain is intentional and documented.")
        if "order by" in lowered and "limit" not in lowered:
            score -= 10
            recommendations.append("Consider whether ordering the full result set is necessary.")
        if "count(distinct" in lowered:
            recommendations.append("Validate whether exact distinct counts are required or whether a pre-aggregated mart would be more cost efficient.")

        if not recommendations:
            recommendations.append("No major heuristic issues found; validate with an explain plan and runtime statistics.")

        return {
            "score": max(score, 0),
            "warnings": warnings,
            "recommendations": recommendations,
        }
