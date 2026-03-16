select
    task_id,
    requester_role,
    request_type,
    environment,
    task_status,
    assigned_agent,
    approval_required,
    submitted_at::timestamp_ntz as submitted_at,
    updated_at::timestamp_ntz as updated_at,
    completed_at::timestamp_ntz as completed_at
from platform.agent_tasks;
