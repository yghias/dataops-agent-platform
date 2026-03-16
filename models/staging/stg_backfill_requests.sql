select
    backfill_request_id,
    task_id,
    asset_name,
    requested_by,
    start_date::date as start_date,
    end_date::date as end_date,
    request_status,
    approval_status,
    requested_at::timestamp_ntz as requested_at,
    approved_at::timestamp_ntz as approved_at
from platform.backfill_requests;
