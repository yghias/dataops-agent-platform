"""Metadata reader for assets and business metrics."""

from __future__ import annotations


class MetadataReader:
    """Mock metadata access layer."""

    def read_asset(self, asset_name: str) -> dict:
        return {
            "asset_name": asset_name,
            "domain": "commercial_analytics",
            "owner": "data-platform",
            "slo": "daily by 06:00 America/Detroit",
            "classification": "internal",
        }

    def read_metric(self, metric_name: str) -> dict:
        return {
            "metric_name": metric_name,
            "canonical_owner": "analytics-engineering",
            "status": "draft",
            "notes": "No canonical definition exists yet in the mock catalog.",
        }
