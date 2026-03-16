select
    execution_event_id,
    task_id,
    recommendation_id,
    execution_status,
    executed_by,
    execution_notes,
    executed_at::timestamp_ntz as executed_at
from platform.execution_events;
