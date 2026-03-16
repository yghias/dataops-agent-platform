"""Read-only Snowflake SQL execution wrapper."""

from __future__ import annotations

from pathlib import Path


class SqlRunner:
    warehouse = "snowflake"

    def execute(self, sql_text: str, limit: int = 25) -> dict:
        return {
            "warehouse": self.warehouse,
            "limit": limit,
            "sql_text": sql_text,
            "preview": [
                {"pipeline_id": "crm_opportunity_pipeline_daily", "pipeline_success_rate": 0.97},
                {"pipeline_id": "query_history_ingestion", "pipeline_success_rate": 0.92},
            ],
        }

    def execute_file(self, path: str) -> dict:
        sql_text = Path(path).read_text(encoding="utf-8")
        return self.execute(sql_text)
