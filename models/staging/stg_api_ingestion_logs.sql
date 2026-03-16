select
    ingestion_log_id,
    source_name,
    endpoint_name,
    http_status::number(10,0) as http_status,
    records_received::number(18,0) as records_received,
    latency_ms::number(18,0) as latency_ms,
    ingestion_status,
    ingested_at::timestamp_ntz as ingested_at
from platform.api_ingestion_logs;
