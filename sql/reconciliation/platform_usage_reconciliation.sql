with task_counts as (
    select request_type, count(*) as task_count
    from platform.agent_tasks
    group by 1
),
mart_counts as (
    select request_type, sum(task_count) as mart_task_count
    from marts.platform_usage_mart
    group by 1
)
select
    t.request_type,
    t.task_count,
    m.mart_task_count
from task_counts t
left join mart_counts m
    on t.request_type = m.request_type
where coalesce(t.task_count, 0) <> coalesce(m.mart_task_count, 0);
