with opportunities as (
    select * from {{ ref('stg_crm_opportunities') }}
),
accounts as (
    select * from {{ ref('stg_crm_accounts') }}
)
select
    o.opportunity_id,
    o.account_id,
    a.account_name,
    a.industry,
    a.region,
    o.opportunity_owner_name,
    o.stage_name,
    o.lifecycle_status,
    o.amount,
    o.probability,
    o.expected_close_date,
    o.close_date,
    coalesce(o.close_date, o.expected_close_date) as reporting_close_date,
    current_date as snapshot_date
from opportunities o
left join accounts a
    on o.account_id = a.account_id;
