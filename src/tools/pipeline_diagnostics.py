"""Pipeline diagnostics helpers for orchestration-facing workflows."""

from __future__ import annotations


class PipelineDiagnostics:
    def render_dag_summary(self, dag_id: str) -> str:
        return (
            f"- DAG: `{dag_id}`\n"
            "- Tasks: ingest_metadata -> validate_contracts -> run_sql_models -> run_quality_checks -> publish_marts\n"
            "- Retries: 3 with exponential backoff\n"
            "- Idempotency: partition/date-based reruns with approval-gated backfill path"
        )
