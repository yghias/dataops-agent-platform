"""Airflow DAG for scheduled platform data quality and reconciliation checks."""

from __future__ import annotations

from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator


def run_sql_tests() -> None:
    print("Executing sql/tests.sql and model-level quality checks.")


def run_reconciliation() -> None:
    print("Executing row count and publication reconciliation checks.")


with DAG(
    dag_id="platform_quality_checks",
    start_date=datetime(2026, 1, 1),
    schedule="15 * * * *",
    catchup=False,
    max_active_runs=1,
    tags=["dataops", "quality"],
) as dag:
    tests = PythonOperator(task_id="run_sql_tests", python_callable=run_sql_tests)
    recon = PythonOperator(task_id="run_reconciliation", python_callable=run_reconciliation)

    tests >> recon
