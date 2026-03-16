"""Mock lineage reader."""

from __future__ import annotations


class LineageTool:
    """Returns simplified lineage edges for impact analysis."""

    def get_lineage(self, asset_name: str) -> dict:
        return {
            "asset": asset_name,
            "upstream": ["raw.crm_orders", "raw.crm_customers"],
            "downstream": ["analytics.orders", "mart_monthly_revenue"],
            "blast_radius": "medium",
        }
