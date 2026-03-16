# Data Model

## Warehouse standard

The platform assumes Snowflake as the primary analytical warehouse. Transformations are modeled as warehouse-native SQL with Airflow orchestrating ingestion and promotion workflows. Python is limited to operational concerns such as request handling, orchestration, API collection, and utility logic.

## Modeling approach

The repository uses a layered model structure:
- `raw`: immutable landed extracts from operational systems
- `staging`: type normalization, naming cleanup, null handling, and source-level filtering
- `intermediate`: business-event preparation and grain alignment
- `marts`: business-facing datasets for reporting, KPI computation, and downstream AI workflows

## Core entities

### `platform.agent_tasks`
- control-plane request intake records
- tracks request type, assigned agent, environment, and approval requirement

### `platform.agent_recommendations`
- generated artifacts emitted by specialist agents
- stores artifact path, confidence score, and review state

### `platform.human_reviews`
- reviewer decisions for generated outputs
- records approval, rejection, revision requests, and notes

### `platform.execution_events`
- post-approval execution records
- links approved recommendations to dry-run or execution events

### `platform.pipeline_runs`
- Airflow and pipeline runtime telemetry
- source of truth for pipeline success rate, retries, and failure analysis

### `platform.query_history`
- Snowflake workload telemetry
- used for cost, latency, and optimization analysis

### `platform.schema_versions`
- upstream schema registry snapshots
- used to detect added, renamed, and type-changed columns

### `raw.crm_accounts`
- account-level source extract
- loaded from CRM API into Snowflake landing tables
- partitioned by `load_date`

### `raw.crm_opportunities`
- opportunity lifecycle data with status, amount, stage, owner, and close dates
- source of truth for pipeline and conversion metrics

### `analytics.dim_account`
- curated account dimension with consistent account identifiers and ownership attributes

### `analytics.fct_opportunity`
- transaction-style opportunity fact table at one row per opportunity snapshot grain

### `analytics.mart_sales_pipeline`
- business-facing mart used by sales operations, analytics, and platform quality monitoring

### `analytics.mart_monthly_active_customers`
- metric mart for monthly active customer reporting and downstream KPI consumers

## Grain rules

- staging models preserve source grain and avoid business aggregations
- intermediate models may reshape events but must state explicit grain in model docs
- marts are the only layer allowed to encode business KPI logic used by reporting consumers
- review comments and AI-generated recommendations should reference the intended grain explicitly

## Snowflake design notes

- use `cluster by` on high-volume fact tables where pruning materially improves runtime
- use transient staging schemas where persistence and fail-safe retention are not required
- store raw ingestion metadata columns such as `_ingested_at`, `_batch_id`, and `_source_file`
- prefer SQL-based incremental loading with deterministic `merge` or append-plus-deduplicate patterns

## Data quality expectations

- primary keys and natural-key uniqueness checks for dimensions
- referential integrity checks between marts and dimensions
- freshness checks for ingestion-facing tables
- reconciliation checks between raw landed row counts and curated publication counts
- metric-level reasonableness checks for business-facing marts
