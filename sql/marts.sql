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

create or replace view marts.agent_review_outcomes_mart as
select
    t.assigned_agent,
    t.request_type,
    t.environment,
    count(r.recommendation_id) as total_recommendations,
    count_if(h.review_decision = 'approved') as approved_recommendations,
    count_if(h.review_decision = 'rejected') as rejected_recommendations,
    round(count_if(h.review_decision = 'approved') / nullif(count(r.recommendation_id), 0), 4) as approval_rate,
    avg(datediff('minute', t.submitted_at, h.reviewed_at)) as avg_minutes_to_review
from platform.agent_tasks t
left join platform.agent_recommendations r
    on t.task_id = r.task_id
left join platform.human_reviews h
    on r.recommendation_id = h.recommendation_id
group by 1, 2, 3;

create or replace view marts.schema_drift_mart as
select
    source_system,
    entity_name,
    drift_type,
    date_trunc('day', effective_at) as effective_day,
    count(*) as drift_events
from platform.schema_versions
where drift_type is not null
group by 1, 2, 3, 4;

create or replace view marts.backfill_operations_mart as
select
    asset_name,
    approval_status,
    request_status,
    count(*) as backfill_requests,
    avg(datediff('day', start_date, end_date)) as avg_backfill_days
from platform.backfill_requests
group by 1, 2, 3;

create or replace view marts.semantic_metrics_mart as
with pipeline_metrics as (
    select
        pipeline_id as metric_entity,
        'pipeline_success_rate' as metric_name,
        pipeline_success_rate::number(18,4) as metric_value,
        latest_completed_at as measured_at
    from marts.pipeline_health_mart
),
quality_metrics as (
    select
        asset_name as metric_entity,
        'data_quality_score' as metric_name,
        data_quality_score::number(18,4) as metric_value,
        measured_day::timestamp_ntz as measured_at
    from marts.data_quality_mart
),
latency_metrics as (
    select
        query_hash as metric_entity,
        'query_latency_ms' as metric_name,
        avg_execution_ms::number(18,4) as metric_value,
        current_timestamp() as measured_at
    from marts.query_performance_mart
)
select * from pipeline_metrics
union all
select * from quality_metrics
union all
select * from latency_metrics;
