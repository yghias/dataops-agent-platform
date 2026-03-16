select
    asset_name,
    approval_status,
    request_status,
    count(*) as backfill_requests,
    avg(datediff('day', start_date, end_date)) as avg_backfill_days,
    min(requested_at) as first_requested_at,
    max(approved_at) as latest_approved_at
from {{ ref('stg_backfill_requests') }}
group by 1, 2, 3;
