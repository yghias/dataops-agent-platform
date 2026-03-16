"""Schema inspection helper."""

from __future__ import annotations


class SchemaInspector:
    def inspect_table(self, table_name: str) -> dict:
        return {
            "table_name": table_name,
            "columns": [
                {"name": "asset_id", "type": "varchar", "nullable": False},
                {"name": "asset_name", "type": "varchar", "nullable": False},
                {"name": "created_at", "type": "timestamp_ntz", "nullable": False},
            ],
            "primary_key": ["asset_id"],
            "warehouse": "snowflake",
        }
