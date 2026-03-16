"""Airflow DAG scaffold generation."""

from __future__ import annotations


class DagGenerator:
    """Generates deterministic DAG scaffolds for review."""

    def generate(self, dag_id: str, schedule: str, source_system: str, target_table: str) -> str:
        return f"""from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


def extract():
    print("Extracting from {source_system}")


def load():
    print("Loading into {target_table}")


with DAG(
    dag_id="{dag_id}",
    start_date=datetime(2024, 1, 1),
    schedule="{schedule}",
    catchup=False,
    max_active_runs=1,
    tags=["dataops-agent-platform", "generated"],
) as dag:
    extract_task = PythonOperator(task_id="extract", python_callable=extract)
    load_task = PythonOperator(task_id="load", python_callable=load)
    extract_task >> load_task
"""
