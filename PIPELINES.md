# Pipelines

## Pipeline families

The platform supports four pipeline families:
- source ingestion
- warehouse transformation
- semantic/reporting publication
- feedback and audit persistence

## Ingestion pattern

Source ingestion is handled by Python where Python adds clear value:
- REST and file-based collection
- authentication and retries
- payload normalization into staged landing files
- orchestration callbacks and control flow

Ingestion design principles:
- idempotent loads by batch ID and logical source window
- explicit retry policy with bounded retries and dead-letter handling
- separation between extraction success and publish success
- warehouse load metadata persisted on every batch

## Transformation pattern

Transformations are SQL-first. Business rules should be expressed in SQL models, not embedded in Python services. Each transformation change should be reviewable as a SQL diff that can be validated independently from orchestration code.

## Airflow operating model

Airflow is the orchestration layer for:
- daily and hourly ingestion DAGs
- dbt or SQL execution tasks
- data quality and reconciliation checks
- backfill and replay workflows
- publication dependencies and downstream alert routing

Standard DAG expectations:
- retries with exponential backoff for transient source failures
- idempotent task behavior
- SLA tagging and alert metadata
- clear boundary between ingestion, transform, validation, and publish tasks

## Failure handling

- ingestion failures should not publish partial curated data
- validation failures should stop downstream promotion
- reconciliation mismatches should raise a reviewable operational event
- approved rollback steps must exist for schema and publication changes
