select
    pipeline_id,
    environment,
    count(*) as total_runs,
    count_if(status = 'success') as successful_runs,
    count_if(status = 'failed') as failed_runs,
    round(count_if(status = 'success') / nullif(count(*), 0), 4) as pipeline_success_rate,
    avg(datediff('second', started_at, ended_at)) as avg_runtime_seconds,
    max(ended_at) as latest_completed_at
from {{ ref('stg_pipeline_runs') }}
group by 1, 2;
