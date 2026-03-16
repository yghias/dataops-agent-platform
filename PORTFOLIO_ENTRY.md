# Platform Summary

`dataops-agent-platform` provides a governed control plane for day-to-day data platform tasks including Snowflake SQL generation, Airflow pipeline creation, schema review, query analysis, observability diagnostics, and runbook generation. The repository includes warehouse schemas, marts, validation queries, specialist agents, tool wrappers, Airflow DAGs, notebooks, and operational documentation.

The implementation keeps business logic in SQL and uses Python primarily for orchestration and integrations. Human review remains mandatory before execution of production-affecting artifacts.
