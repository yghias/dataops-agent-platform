# Backfill Strategy

## Goals

- rebuild historical partitions safely
- preserve idempotent behavior
- prevent duplicate publication
- re-run validation and reconciliation before publish

## Backfill workflow

1. submit a backfill task with affected assets and date range
2. validate approval requirements based on environment and blast radius
3. rerun raw-to-staging loads for selected partitions
4. rerun incremental or partition-scoped SQL models
5. rerun `sql/tests.sql` and reconciliation checks
6. publish only after review

## Idempotency strategy

- use partition/date-range filtering in Airflow backfill DAGs
- merge or replace partitions rather than blind append
- keep `_batch_id` and `request_id` for replay traceability

## Rollback

- restore prior mart snapshot or rerun previous approved artifact set
- log rollback in execution events and human review history
