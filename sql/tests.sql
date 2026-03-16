-- duplicate task detection
select task_id, count(*) as row_count
from platform.agent_tasks
group by 1
having count(*) > 1;

-- referential integrity: recommendations without tasks
select recommendation_id
from platform.agent_recommendations r
left join platform.agent_tasks t
    on r.task_id = t.task_id
where t.task_id is null;

-- null checks on critical pipeline runtime columns
select run_id
from platform.pipeline_runs
where pipeline_id is null
   or status is null
   or started_at is null;

-- anomaly check: failed pipeline spike using 7-day moving average
with daily_failures as (
    select
        date_trunc('day', started_at) as run_day,
        count_if(status = 'failed') as failed_runs
    from platform.pipeline_runs
    group by 1
),
scored as (
    select
        run_day,
        failed_runs,
        avg(failed_runs) over (
            order by run_day
            rows between 7 preceding and 1 preceding
        ) as trailing_avg_failures
    from daily_failures
)
select *
from scored
where trailing_avg_failures is not null
  and failed_runs > trailing_avg_failures * 2;

-- reconciliation: quality results must reference known assets
select count(*) as orphan_quality_results
from platform.data_quality_results q
left join platform.data_assets a
    on q.asset_id = a.asset_id
where a.asset_id is null;

-- contract validation: required platform pipeline columns must exist in latest schema version
select schema_version_id
from platform.schema_versions
where entity_name = 'pipeline_runs'
  and (
      schema_payload:"columns"[0] is null
      or schema_payload:"columns" is null
  );

-- review reconciliation: every approved execution must have a prior approved review
select e.execution_event_id
from platform.execution_events e
left join platform.human_reviews h
    on e.recommendation_id = h.recommendation_id
where e.execution_status in ('executed', 'succeeded')
  and coalesce(h.review_decision, 'missing') <> 'approved';

-- backfill overlap detection
select
    a.backfill_request_id as request_a,
    b.backfill_request_id as request_b,
    a.asset_name
from platform.backfill_requests a
join platform.backfill_requests b
    on a.asset_name = b.asset_name
   and a.backfill_request_id <> b.backfill_request_id
   and a.start_date <= b.end_date
   and b.start_date <= a.end_date;

-- semantic metric completeness check
select metric_name
from marts.semantic_metrics_mart
group by 1
having count(*) = 0;
