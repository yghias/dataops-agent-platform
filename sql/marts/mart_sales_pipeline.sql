select
    snapshot_date,
    region,
    opportunity_owner_name,
    lifecycle_status,
    count(*) as opportunity_count,
    sum(amount) as pipeline_amount,
    sum(case when lifecycle_status = 'CLOSED_WON' then amount else 0 end) as closed_won_amount
from intermediate.int_opportunity_daily_snapshot
group by 1, 2, 3, 4;
