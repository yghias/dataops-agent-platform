"""Airflow DAG for platform mart refresh."""

from __future__ import annotations

from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator


def refresh_platform_models() -> None:
    print("Refreshing staging, intermediate, and mart SQL assets.")


with DAG(
    dag_id="platform_marts_refresh",
    start_date=datetime(2026, 1, 1),
    schedule="30 * * * *",
    catchup=False,
    max_active_runs=1,
    tags=["dataops", "marts"],
) as dag:
    refresh = PythonOperator(task_id="refresh_platform_models", python_callable=refresh_platform_models)
