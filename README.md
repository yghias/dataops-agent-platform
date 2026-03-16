# dataops-agent-platform

`dataops-agent-platform` is a governed multi-agent platform for data engineering, architecture, database, analytics, cloud platform, and AI/ML operating workflows. The service generates reviewable drafts for SQL models, Airflow DAGs, warehouse checks, architecture decisions, runbooks, and operational guidance while preserving explicit human approval before execution or promotion.

The repository is organized as an internal engineering platform codebase. It emphasizes:
- specialist agents instead of a single general assistant
- policy-aware routing and tool access
- explicit human review before execution
- auditability, feedback capture, and reusable memory
- SQL-first warehouse modeling with Snowflake as the reference platform
- strong documentation and operational structure

## Platform responsibilities

The platform accepts a request, classifies it, routes it to the right specialist agents, invokes constrained tools, generates draft outputs, runs a reviewer pass, and packages results for human approval. Approved outputs can then move into a controlled execution workflow, while rejected outputs are logged for continuous improvement.

Primary request families:
- ETL/ELT pipeline generation
- Airflow DAG creation
- Snowflake SQL model and test generation
- SQL generation and optimization
- schema and data model review
- architecture review and platform guidance
- CI/CD and cloud platform recommendations
- data quality and observability design
- documentation and runbook generation
- feature pipeline and ML workflow support

## Platform boundaries

- Agents may inspect metadata, generate SQL, propose DAGs, and assemble review packages.
- Agents may not execute production changes without approval.
- Transformations belong in SQL models wherever practical.
- Python is reserved for ingestion, orchestration, workflow control, integrations, and ML-specific utilities.

## Repository layout

At a high level, the repository contains:
- `agents/`: specialist agents with clear input and output contracts
- `tools/`: adapters for SQL execution, metadata, lineage, query analysis, documentation, and quality checks
- `workflows/`: intake, approval, execution, and feedback flows
- `memory/`: prompt registry, decision logging, and feedback storage
- `governance/`: approval and audit operating model
- `models/`: dbt-style Snowflake models and model-level tests
- `sql/`: DDL, marts, quality checks, and reconciliation queries
- `sample_data/`: source payload and warehouse sample data references
- `infrastructure/`: baseline deployment and environment notes

Reference docs:
- [`ARCHITECTURE.md`](/Users/yasserghias/Documents/Playground/dataops-agent-platform/ARCHITECTURE.md)
- [`DATA_MODEL.md`](/Users/yasserghias/Documents/Playground/dataops-agent-platform/DATA_MODEL.md)
- [`PIPELINES.md`](/Users/yasserghias/Documents/Playground/dataops-agent-platform/PIPELINES.md)
- [`WORKFLOWS.md`](/Users/yasserghias/Documents/Playground/dataops-agent-platform/WORKFLOWS.md)
- [`GOVERNANCE.md`](/Users/yasserghias/Documents/Playground/dataops-agent-platform/GOVERNANCE.md)

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m workflows.intake_workflow
```

## Development assumptions

- warehouse: Snowflake
- orchestration: Airflow
- transformation style: SQL-heavy, dbt-style model layout
- deployment environments: `dev`, `staging`, `prod`
- approval requirement: mandatory for production-impacting outputs

## Operating model

1. Intake workflow normalizes a request and selects specialist agents.
2. Selected agents gather schema, lineage, metadata, and SQL context.
3. SQL-first artifacts are generated for transformations, marts, tests, and reporting logic.
4. Reviewer and quality logic package the result for human approval.
5. Approved artifacts move into execution controls, audit logs, and feedback capture.

## Review path

Start with these files:
1. [`ARCHITECTURE.md`](/Users/yasserghias/Documents/Playground/dataops-agent-platform/ARCHITECTURE.md)
2. [`DATA_MODEL.md`](/Users/yasserghias/Documents/Playground/dataops-agent-platform/DATA_MODEL.md)
3. [`models/marts/mart_sales_pipeline.sql`](/Users/yasserghias/Documents/Playground/dataops-agent-platform/models/marts/mart_sales_pipeline.sql)
4. [`workflows/intake_workflow.py`](/Users/yasserghias/Documents/Playground/dataops-agent-platform/workflows/intake_workflow.py)
5. [`tools/query_optimizer.py`](/Users/yasserghias/Documents/Playground/dataops-agent-platform/tools/query_optimizer.py)
6. [`governance/approval_policy.md`](/Users/yasserghias/Documents/Playground/dataops-agent-platform/governance/approval_policy.md)
