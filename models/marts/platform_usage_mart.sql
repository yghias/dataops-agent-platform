select
    request_type,
    assigned_agent,
    environment,
    count(*) as task_count,
    count_if(task_status = 'completed') as completed_tasks,
    count_if(task_status = 'rejected') as rejected_tasks
from platform.agent_tasks
group by 1, 2, 3;
