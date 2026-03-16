"""Read-only Snowflake SQL runner abstraction."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass
class SqlExecutionResult:
    warehouse: str
    query: str
    row_count: int
    columns: list[str]
    preview: list[dict[str, Any]]
    mode: str


class SqlRunner:
    """Executes parameterized, read-only SQL.

    The class is intentionally lightweight. It mirrors the contract expected by
    agents without coupling the repository to a live Snowflake connection.
    """

    warehouse = "snowflake"

    def execute(self, query: str, limit: int = 25, read_only: bool = True) -> SqlExecutionResult:
        mode = "read_only" if read_only else "unsafe_write_disabled"
        return SqlExecutionResult(
            warehouse=self.warehouse,
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

    def execute_file(self, path: str | Path, limit: int = 25) -> SqlExecutionResult:
        sql_path = Path(path)
        query = sql_path.read_text(encoding="utf-8")
        return self.execute(query=query, limit=limit, read_only=True)

    def explain(self, query: str) -> dict[str, Any]:
        return {
            "warehouse": self.warehouse,
            "query": query,
            "plan_summary": "Scan on analytics.orders with partition pruning opportunity on order_ts and hash join to analytics.customers",
            "estimated_cost": 82431,
            "suggested_actions": [
                "project only required columns",
                "filter earlier on the cluster or partition key",
                "avoid broad scans on unbounded date ranges",
                "review join key distribution and clustering strategy",
            ],
        }
