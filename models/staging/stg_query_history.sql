select
    query_id,
    warehouse_name,
    user_name,
    schema_name,
    query_text,
    query_hash,
    bytes_scanned::number(38,0) as bytes_scanned,
    rows_produced::number(38,0) as rows_produced,
    execution_ms::number(18,0) as execution_ms,
    started_at::timestamp_ntz as started_at,
    completed_at::timestamp_ntz as completed_at
from platform.query_history;
