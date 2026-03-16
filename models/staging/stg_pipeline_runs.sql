select
    run_id,
    pipeline_id,
    dag_id,
    lower(status) as status,
    started_at::timestamp_ntz as started_at,
    ended_at::timestamp_ntz as ended_at,
    retry_count::number(10,0) as retry_count,
    error_class,
    error_message,
    environment
from platform.pipeline_runs;
