select
    schema_name,
    query_hash,
    count(*) as executions,
    avg(execution_ms) as avg_execution_ms,
    max(execution_ms) as max_execution_ms,
    avg(bytes_scanned) as avg_bytes_scanned,
    rank() over (partition by schema_name order by avg(execution_ms) desc) as slow_query_rank
from {{ ref('stg_query_history') }}
group by 1, 2;
