# Tools

## Tooling philosophy

Tools are modeled as constrained platform capabilities, not arbitrary function calls. Each tool should:
- have a narrow purpose
- define input and output shape
- advertise read/write/execute risk
- support logging and evidence capture
- make warehouse-facing logic reviewable independently from orchestration code

## Current tools

### SQL Runner
Executes read-only Snowflake SQL, explain plans, and bounded result previews with request-level audit metadata.

### Schema Inspector
Returns column, datatype, primary key, foreign key, and table-level metadata used by modeling and optimization agents.

### Metadata Reader
Provides logical ownership, SLA, stewardship, and classification details for warehouse objects.

### Lineage Tool
Supplies upstream and downstream context to help agents estimate change impact and incident blast radius.

### Query Optimizer
Runs heuristic checks over SQL text to identify anti-patterns and provide targeted rewrite guidance.

### DAG Generator
Builds Airflow DAG scaffolds with retries, SLA hooks, task grouping, and idempotent load patterns.

### dbt Generator
Creates dbt-style SQL models, tests, source YAML, and documentation blocks aligned to warehouse-first transformation practices.

### Documentation Generator
Assembles technical docs and runbooks from structured inputs such as assumptions, failure modes, owners, and remediation steps.

### Quality Checker
Runs lightweight validations over artifacts before review or execution.

## Production migration path

The tool interfaces in this repository are intentionally simple. They can be backed later by:
- warehouse connectors
- metadata catalogs
- lineage APIs
- ticketing systems
- secret managers
- policy engines

That migration path is part of what makes the repository realistic for senior-level discussion.
