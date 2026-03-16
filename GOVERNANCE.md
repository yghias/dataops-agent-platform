# Governance

## Objective

The governance model ensures the platform accelerates work without weakening engineering controls. It formalizes how requests are reviewed, how risky actions are blocked or escalated, and how decisions remain auditable.

## Core governance principles

- humans approve all impactful outputs
- least privilege applies to tools and data access
- production changes require stronger review than draft generation
- decisions must include rationale
- logs and artifacts must be traceable and reviewable

## Policy categories

### Access policy
Controls who can inspect metadata, execute queries, review artifacts, and authorize execution.

### Environment policy
Constrains actions by environment. Development requests may allow more experimentation; production requests require stricter review and often dual approval.

### Data sensitivity policy
Controls how schema details, metadata, and outputs are handled for sensitive or regulated datasets.

### Change policy
Defines which artifacts are generation-only and which may proceed to execution after approval.

## Review model

Minimum review expectations:
- documentation drafts: one reviewer
- SQL optimization advice: one domain reviewer
- schema-impacting proposals: database or architecture reviewer
- deployment-affecting changes: platform reviewer
- production execution: authorized approver and audit record

## Approval matrix

| Change type | Minimum reviewer | Additional requirements |
| --- | --- | --- |
| KPI SQL change | Analytics engineering | Business owner sign-off if canonical metric changes |
| Snowflake mart change | Data engineering | Warehouse validation and reconciliation queries |
| Schema or DDL recommendation | DBA or data architect | Rollback and maintenance window plan |
| Airflow DAG change | Data engineering | Retry and idempotency review |
| Production execution request | Authorized approver | Prior approved artifact and execution logging |

## Continuous improvement

Governance data should be used to identify:
- common rejection patterns
- tool misuse risk
- weak prompt templates
- roles that need more tailored approval pathways

The platform becomes more trustworthy over time when governance is treated as an engineering feedback loop rather than a compliance tax.
