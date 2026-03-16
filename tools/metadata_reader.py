"""Metadata reader for Snowflake assets and business metrics."""

from __future__ import annotations


class MetadataReader:
    """Returns static metadata aligned to the SQL assets in this repository."""

    def read_asset(self, asset_name: str) -> dict:
        return {
            "asset_name": asset_name,
            "domain": "commercial_analytics",
            "owner": "data-platform",
            "slo": "daily by 06:00 America/Detroit",
            "classification": "internal",
            "warehouse": "snowflake",
            "steward": "analytics-engineering",
        }

    def read_metric(self, metric_name: str) -> dict:
        return {
            "metric_name": metric_name,
            "canonical_owner": "analytics-engineering",
            "status": "draft",
            "notes": "Metric should be sourced from SQL in models/marts and reviewed before publication.",
        }
