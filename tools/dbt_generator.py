"""dbt model and test scaffold generation."""

from __future__ import annotations


class DbtGenerator:
    """Generates dbt-ready SQL and YAML stubs."""

    def generate_model(self, model_name: str, source_name: str, source_table: str) -> dict[str, str]:
        sql = (
            f"select\n"
            f"    customer_id,\n"
            f"    order_id,\n"
            f"    order_ts,\n"
            f"    gross_revenue\n"
            f"from {{{{ source('{source_name}', '{source_table}') }}}}\n"
            f"where order_ts >= current_date - interval '30 day'"
        )
        yaml = (
            "version: 2\n"
            "models:\n"
            f"  - name: {model_name}\n"
            "    columns:\n"
            "      - name: order_id\n"
            "        tests: [not_null, unique]\n"
        )
        return {"sql": sql, "yaml": yaml}
