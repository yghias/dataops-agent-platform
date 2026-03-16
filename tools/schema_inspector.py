"""Schema inspection helper."""

from __future__ import annotations


class SchemaInspector:
    """Returns warehouse-like table metadata for agent grounding."""

    def inspect_table(self, table_name: str) -> dict:
        return {
            "table_name": table_name,
            "owner": "data-platform",
            "columns": [
                {"name": "customer_id", "type": "bigint", "nullable": False},
                {"name": "order_id", "type": "bigint", "nullable": False},
                {"name": "order_ts", "type": "timestamp", "nullable": False},
                {"name": "gross_revenue", "type": "numeric(18,2)", "nullable": False},
            ],
            "primary_key": ["order_id"],
            "foreign_keys": [{"column": "customer_id", "references": "analytics.customers.customer_id"}],
            "partitioning": {"method": "range", "column": "order_ts"},
        }
