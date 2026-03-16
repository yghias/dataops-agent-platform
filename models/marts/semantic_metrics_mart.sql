with pipeline_metrics as (
    select
        pipeline_id as metric_entity,
        'pipeline_success_rate' as metric_name,
        pipeline_success_rate::number(18,4) as metric_value,
        latest_completed_at as measured_at
    from {{ ref('pipeline_health_mart') }}
),
quality_metrics as (
    select
        asset_name as metric_entity,
        'data_quality_score' as metric_name,
        data_quality_score::number(18,4) as metric_value,
        measured_day::timestamp_ntz as measured_at
    from {{ ref('data_quality_mart') }}
),
latency_metrics as (
    select
        query_hash as metric_entity,
        'query_latency_ms' as metric_name,
        avg_execution_ms::number(18,4) as metric_value,
        current_timestamp() as measured_at
    from {{ ref('query_performance_mart') }}
)
select * from pipeline_metrics
union all
select * from quality_metrics
union all
select * from latency_metrics;
