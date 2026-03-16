create or replace view marts.pipeline_health_mart as
select
    pipeline_id,
    environment,
    count(*) as total_runs,
    count_if(status = 'success') as successful_runs,
    count_if(status = 'failed') as failed_runs,
    round(count_if(status = 'success') / nullif(count(*), 0), 4) as pipeline_success_rate,
    avg(datediff('second', started_at, ended_at)) as avg_runtime_seconds,
    max(ended_at) as latest_completed_at
from platform.pipeline_runs
group by 1, 2;

create or replace view marts.data_quality_mart as
select
    a.asset_name,
    a.domain_name,
    date_trunc('day', q.measured_at) as measured_day,
    count(*) as executed_checks,
    count_if(q.status = 'pass') as passed_checks,
    count_if(q.status = 'fail') as failed_checks,
    round(count_if(q.status = 'pass') / nullif(count(*), 0), 4) as data_quality_score
from platform.data_quality_results q
join platform.data_assets a
    on q.asset_id = a.asset_id
group by 1, 2, 3;

create or replace view marts.query_performance_mart as
select
    schema_name,
    query_hash,
    count(*) as executions,
    avg(execution_ms) as avg_execution_ms,
    max(execution_ms) as max_execution_ms,
    avg(bytes_scanned) as avg_bytes_scanned,
    row_number() over (partition by schema_name order by avg(execution_ms) desc) as slow_query_rank
from platform.query_history
group by 1, 2;

create or replace view marts.platform_usage_mart as
select
    request_type,
    assigned_agent,
    environment,
    count(*) as task_count,
    count_if(task_status = 'completed') as completed_tasks,
    count_if(task_status = 'rejected') as rejected_tasks,
    min(submitted_at) as first_task_at,
    max(completed_at) as latest_completion_at
from platform.agent_tasks
group by 1, 2, 3;
