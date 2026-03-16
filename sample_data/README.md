# Sample Data

This directory holds non-sensitive datasets used to reproduce common platform issues and validate warehouse models.

## Included scenarios

- pipeline failures from Airflow metadata
- late arriving data affecting freshness checks
- schema drift events from the registry
- duplicates in landed operational datasets
- slow query patterns in warehouse query history
- repeated quality-result records for duplicate detection tests

## Contents

- `requests/`: task payloads used by orchestration examples
- `warehouse/`: CSV datasets aligned to Snowflake staging and mart logic
