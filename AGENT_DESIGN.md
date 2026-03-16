# Agent Design

## Overview

The platform uses specialist agents to keep task generation aligned to domain ownership and review expectations. Each agent operates within a bounded tool set and emits structured artifacts suitable for human review.

## Shared operating contract

Each agent receives:
- `task_id`
- `request_type`
- `environment`
- `requester_role`
- normalized payload and contextual metadata

Each agent returns:
- artifact type
- rendered content
- rationale
- assumptions
- warnings
- evidence collected from tools
- recommended next action

## Agent responsibilities

### Data Engineer Agent
- generates Snowflake SQL transformations
- drafts Airflow DAGs and dbt-style models
- recommends incremental loading, idempotency, and backfill handling

### Data Architect Agent
- proposes conceptual, logical, and physical models
- defines canonical entities and data contract boundaries
- reviews grain, ownership, and schema evolution risk

### Cloud Data Platform Agent
- recommends storage and compute configuration
- proposes cost control and environment separation strategies
- documents warehouse and orchestration deployment assumptions

### Database Engineer Agent
- reviews SQL shape and runtime behavior
- proposes clustering, partitioning, and performance improvements
- interprets query patterns against Snowflake workload behavior

### DBA Agent
- reviews production-safety implications
- recommends maintenance controls, health checks, and rollback expectations
- validates execution boundaries for warehouse changes

### Data Analyst Agent
- generates KPI SQL and semantic metric definitions
- translates business questions into reusable marts and reporting logic

### Data Scientist Agent
- designs feature datasets and experiment input tables
- proposes training data preparation and validation logic

### AI/ML Engineer Agent
- proposes model-serving and evaluation pipeline structure
- recommends retrieval and evaluation patterns for AI workloads

### Observability Agent
- analyzes pipeline failures, freshness breaches, and anomaly signals
- recommends warehouse and orchestration checks

### Documentation Agent
- produces runbooks, ADRs, lineage notes, and operational summaries

## Routing policy

Routing is deterministic in the repository version:
- pipeline and dbt tasks -> Data Engineer Agent
- schema and contract tasks -> Data Architect Agent
- cost and environment tasks -> Cloud Data Platform Agent
- slow query and database review tasks -> Database Engineer Agent + DBA Agent
- KPI and reporting tasks -> Data Analyst Agent
- feature and experiment tasks -> Data Scientist Agent
- model pipeline and retrieval tasks -> AI/ML Engineer Agent
- failure/debugging tasks -> Observability Agent
- document-only tasks -> Documentation Agent

## Review boundary

Agents may generate proposals but may not approve or execute production changes. Reviewers remain responsible for final acceptance, and execution is handled by workflow controls after approval.
