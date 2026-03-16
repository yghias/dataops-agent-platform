# API Integrations

## Purpose

The platform ingests metadata and operational evidence from APIs and system exports rather than relying on direct warehouse-only introspection. This keeps recommendations grounded in platform state, lineage, and runtime conditions.

## Supported integration types

### Airflow metadata
Use cases:
- pipeline health analysis
- DAG run failure diagnostics
- retry and SLA review

Example payload:
```json
{
  "dag_id": "crm_opportunity_pipeline_daily",
  "run_id": "scheduled__2026-03-16T05:00:00+00:00",
  "state": "failed",
  "start_date": "2026-03-16T05:00:00Z",
  "end_date": "2026-03-16T05:07:18Z",
  "failed_tasks": ["validate_contract", "publish_mart"]
}
```

### Schema registry
Use cases:
- contract enforcement
- schema drift detection
- upstream change review

Example payload:
```json
{
  "source_system": "crm",
  "entity": "opportunities",
  "version": 12,
  "columns": [
    {"name": "opportunity_id", "type": "string", "nullable": false},
    {"name": "account_id", "type": "string", "nullable": false},
    {"name": "win_probability", "type": "decimal(5,2)", "nullable": true}
  ]
}
```

### Data catalog / metadata service
Use cases:
- ownership lookup
- criticality and SLA context
- steward and domain assignment

### Monitoring and alert systems
Use cases:
- anomaly and freshness alert context
- severity and impact analysis
- incident debugging

### Warehouse query history
Use cases:
- slow query analysis
- bytes scanned and runtime review
- repeated anti-pattern detection

## Authentication assumptions

- service-to-service auth via environment-specific credentials
- secrets injected through runtime environment or secret manager
- read-only access for metadata APIs by default

## Failure handling

- API collectors should use bounded retries
- malformed payloads should land in quarantine tables
- critical metadata feeds should emit alertable ingestion failures
