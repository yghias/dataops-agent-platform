"""Mock SQL runner with read-only execution semantics."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class SqlExecutionResult:
    query: str
    row_count: int
    columns: list[str]
    preview: list[dict[str, Any]]
    mode: str


class SqlRunner:
    """Executes parameterized, read-only SQL in demo mode."""

    def execute(self, query: str, limit: int = 25, read_only: bool = True) -> SqlExecutionResult:
        mode = "read_only" if read_only else "unsafe_write_disabled"
        return SqlExecutionResult(
            query=query,
            row_count=min(limit, 3),
            columns=["customer_id", "order_count", "gross_revenue"],
            preview=[
                {"customer_id": 101, "order_count": 14, "gross_revenue": 1200.50},
                {"customer_id": 202, "order_count": 8, "gross_revenue": 845.10},
                {"customer_id": 309, "order_count": 3, "gross_revenue": 212.75},
            ],
            mode=mode,
        )

    def explain(self, query: str) -> dict[str, Any]:
        return {
            "query": query,
            "plan_summary": "Sequential scan on analytics.orders with hash join to analytics.customers",
            "estimated_cost": 82431,
            "suggested_actions": [
                "reduce projected columns",
                "filter earlier on partition key",
                "verify join key distribution and indexing strategy",
            ],
        }
