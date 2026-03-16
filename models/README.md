# Models

This directory contains dbt-style Snowflake models used as the preferred expression of transformation and KPI logic.

## Layout

- `staging/`: source cleanup and type normalization
- `intermediate/`: business-event reshaping and grain alignment
- `marts/`: consumer-facing datasets and KPI marts
- `tests/`: warehouse assertions and reconciliation checks

## Modeling conventions

- use `stg_` for staging models
- use `int_` for intermediate models
- use `mart_` for business-facing publication datasets
- keep business logic in SQL models, not orchestration code
- document grain and key assumptions in model comments or YAML
