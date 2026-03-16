"""dbt-style Snowflake model and test scaffold generation."""

from __future__ import annotations


class DbtGenerator:
    """Generates dbt-ready SQL and YAML stubs."""

    def generate_model(self, model_name: str, source_name: str, source_table: str) -> dict[str, str]:
        sql = (
            "{{ config(materialized='incremental', unique_key='order_id', on_schema_change='sync_all_columns') }}\n\n"
            f"select\n"
            f"    customer_id,\n"
            f"    order_id,\n"
            f"    order_ts,\n"
            f"    gross_revenue\n"
            f"from {{{{ source('{source_name}', '{source_table}') }}}}\n"
            f"where order_ts >= dateadd(day, -30, current_date)\n"
            "{% if is_incremental() %}\n"
            "  and order_ts >= (select coalesce(max(order_ts), '1900-01-01') from {{ this }})\n"
            "{% endif %}"
        )
        yaml = (
            "version: 2\n"
            "models:\n"
            f"  - name: {model_name}\n"
            "    description: Curated incremental model generated from a governed platform request.\n"
            "    columns:\n"
            "      - name: order_id\n"
            "        tests: [not_null, unique]\n"
        )
        return {"sql": sql, "yaml": yaml}
