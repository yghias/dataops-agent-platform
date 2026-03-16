"""Small local dbt-style SQL generator used by src runtime."""

from __future__ import annotations


class DbtGeneratorShim:
    def generate_model(self, model_name: str, source_name: str, source_table: str) -> dict[str, str]:
        return {
            "sql": (
                "{{ config(materialized='incremental', unique_key='run_id') }}\n"
                "select *\n"
                f"from {{{{ source('{source_name}', '{source_table}') }}}}\n"
            ),
            "yaml": (
                "version: 2\n"
                "models:\n"
                f"  - name: {model_name}\n"
                "    columns:\n"
                "      - name: run_id\n"
                "        tests: [not_null, unique]\n"
            ),
        }
