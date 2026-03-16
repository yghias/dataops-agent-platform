select
    snapshot_date,
    region,
    industry,
    opportunity_owner_name,
    lifecycle_status,
    stage_name,
    count(*) as opportunity_count,
    sum(amount) as pipeline_amount,
    sum(case when lifecycle_status = 'CLOSED_WON' then amount else 0 end) as closed_won_amount,
    sum(case when lifecycle_status = 'OPEN' then amount else 0 end) as open_pipeline_amount,
    avg(probability) as avg_probability,
    count_if(reporting_close_date between current_date and current_date + 30) as opportunities_due_in_30_days
from {{ ref('int_opportunity_daily_snapshot') }}
group by 1, 2, 3, 4, 5, 6;
