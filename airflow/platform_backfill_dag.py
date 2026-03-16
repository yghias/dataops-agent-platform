"""Airflow DAG for approval-gated historical backfills."""

from __future__ import annotations

from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator


def rebuild_partitions() -> None:
    print("Rebuilding approved historical partitions.")


def rerun_validation() -> None:
    print("Rerunning validation and reconciliation after backfill.")


with DAG(
    dag_id="platform_backfill_reprocessing",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    max_active_runs=1,
    tags=["dataops", "backfill"],
) as dag:
    rebuild = PythonOperator(task_id="rebuild_partitions", python_callable=rebuild_partitions)
    validate = PythonOperator(task_id="rerun_validation", python_callable=rerun_validation)

    rebuild >> validate
