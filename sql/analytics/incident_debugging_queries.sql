-- recent failures with associated quality regressions
select
    r.pipeline_id,
    r.run_id,
    r.error_class,
    r.error_message,
    q.check_name,
    q.measured_value,
    q.threshold_value
from platform.pipeline_runs r
left join platform.data_quality_results q
    on r.run_id = q.run_id
where r.status = 'failed'
order by r.started_at desc;

-- slow queries with high bytes scanned
select
    schema_name,
    query_hash,
    avg(execution_ms) as avg_execution_ms,
    avg(bytes_scanned) as avg_bytes_scanned
from platform.query_history
group by 1, 2
having avg(execution_ms) > 5000
   or avg(bytes_scanned) > 100000000;
