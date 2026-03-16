with history as (
    select * from {{ ref('stg_query_history') }}
)
select
    query_id,
    schema_name,
    query_hash,
    execution_ms,
    bytes_scanned,
    rows_produced,
    iff(rows_produced = 0, null, bytes_scanned / rows_produced) as bytes_per_row,
    avg(execution_ms) over (
        partition by query_hash
        order by started_at
        rows between 10 preceding and 1 preceding
    ) as trailing_avg_execution_ms,
    avg(bytes_scanned) over (
        partition by query_hash
        order by started_at
        rows between 10 preceding and 1 preceding
    ) as trailing_avg_bytes_scanned
from history;
