with runs as (
    select * from {{ ref('stg_pipeline_runs') }}
),
quality as (
    select * from {{ ref('stg_data_quality_results') }}
),
joined as (
    select
        r.run_id,
        r.pipeline_id,
        r.environment,
        r.status,
        r.error_class,
        r.error_message,
        r.started_at,
        count_if(q.status = 'fail') as failed_checks,
        avg(q.measured_value) as avg_measured_value
    from runs r
    left join quality q
        on r.run_id = q.run_id
    group by 1, 2, 3, 4, 5, 6, 7
)
select
    *,
    avg(failed_checks) over (
        partition by pipeline_id, environment
        order by started_at
        rows between 7 preceding and 1 preceding
    ) as trailing_failed_checks_avg
from joined;
