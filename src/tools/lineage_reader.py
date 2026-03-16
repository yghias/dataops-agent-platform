"""Lineage reader for warehouse assets."""

from __future__ import annotations


class LineageReader:
    def read_lineage(self, asset_name: str) -> dict:
        return {
            "asset_name": asset_name,
            "upstream": ["raw.pipeline_runs", "raw.query_history"],
            "downstream": ["marts.pipeline_health_mart", "marts.query_performance_mart"],
        }
