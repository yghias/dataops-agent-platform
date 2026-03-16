select
    a.asset_name,
    a.domain_name,
    date_trunc('day', q.measured_at) as measured_day,
    count(*) as executed_checks,
    count_if(q.status = 'pass') as passed_checks,
    count_if(q.status = 'fail') as failed_checks,
    round(count_if(q.status = 'pass') / nullif(count(*), 0), 4) as data_quality_score
from platform.data_quality_results q
join {{ ref('stg_data_assets') }} a
    on q.asset_id = a.asset_id
group by 1, 2, 3;
