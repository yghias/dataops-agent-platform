# Data Contracts

## Purpose

Data contracts define the expected shape of upstream operational feeds before they are accepted into Snowflake staging models. Contract validation is part of ingestion and must succeed before downstream publication.

## Contracted sources

### `crm.opportunities`

Required columns:
- `opportunity_id` `string`
- `account_id` `string`
- `owner_name` `string`
- `stage_name` `string`
- `amount` `decimal(18,2)`
- `expected_close_date` `date`

Optional columns:
- `close_date` `date`
- `probability` `decimal(5,2)`

Validation rules:
- `opportunity_id` must be unique per source version
- `amount` must be greater than or equal to `0`
- `stage_name` must be one of `OPEN`, `QUALIFIED`, `COMMIT`, `CLOSED_WON`, `CLOSED_LOST`

### `platform.pipeline_runs`

Required columns:
- `run_id` `string`
- `pipeline_id` `string`
- `dag_id` `string`
- `status` `string`
- `started_at` `timestamp`
- `environment` `string`

Validation rules:
- `status` must be one of `success`, `failed`, `running`, `queued`
- `retry_count` must be greater than or equal to `0`

## Enforcement

Contract checks run:
- during ingestion DAG execution
- before dbt-style staging publication
- before backfill publication for historical rebuilds

Contract violations:
- block downstream publication
- generate an operational event
- require review if drift impacts canonical marts
