-- backfills awaiting approval should not be executed
select backfill_request_id
from platform.backfill_requests
where request_status = 'executing'
  and approval_status <> 'approved';

-- overlapping backfill windows for the same asset
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
