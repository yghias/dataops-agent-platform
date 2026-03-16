"""Metadata reader."""

from __future__ import annotations


class MetadataReader:
    def read_asset(self, asset_name: str) -> dict:
        return {
            "asset_name": asset_name,
            "owner_role": "data_platform",
            "criticality": "high",
            "warehouse": "snowflake",
            "sla_minutes": 60,
        }
