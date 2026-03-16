# Observability

## Objective

Observability in this platform serves two purposes:
- operate the platform itself
- help agents generate and review observability for data systems

## Platform observability

Recommended signals:
- request volume by task type
- routing accuracy and fallback rate
- agent latency and failure rate
- tool latency and error rate
- approval turnaround time
- rejection rate by artifact type
- execution success rate for approved artifacts
- Snowflake validation pass rate by model and mart
- Airflow task retry counts for generated DAGs
- backfill run success rate and partition completion lag

## Artifact quality observability

Generated outputs should be measured for:
- completeness
- standards compliance
- human approval rate
- revision frequency
- downstream execution success

## Traceability model

Every task should be traceable across:
- request
- route decision
- tool evidence
- agent draft
- reviewer notes
- human decision
- execution outcome

## Operational dashboards

The repository proposes dashboard groups for:
- platform operations
- artifact quality
- governance and approvals
- Snowflake model freshness and reconciliation health

See [`dashboards/metrics.md`](dashboards/metrics.md) for suggested KPIs.
