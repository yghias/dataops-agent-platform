# Cost And Performance

## Snowflake controls

- use incremental marts for query history, pipeline health, and quality summaries
- cluster high-volume telemetry by event date and high-cardinality join keys where justified
- isolate ingestion, transform, and diagnostic workloads onto separate warehouses
- use auto-suspend and bounded backfill windows to control spend

## Query performance practices

- avoid repeated `select *` on mart-facing queries
- publish pre-aggregated platform marts for recurring dashboards
- prefer bounded time filters and partition-aware predicates
- review bytes scanned against expected workload class

## Backfill cost controls

- require date-range scoping
- require impact estimate for large historical rebuilds
- publish cost warnings in review packages for long-range backfills
