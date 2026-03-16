with source_opportunities as (
    select
        opportunity_id::varchar as opportunity_id,
        account_id::varchar as account_id,
        owner_name::varchar as opportunity_owner_name,
        upper(trim(stage_name))::varchar as stage_name,
        amount::number(18,2) as amount,
        probability::number(5,2) as probability,
        expected_close_date::date as expected_close_date,
        close_date::date as close_date,
        case
            when is_closed_won then 'CLOSED_WON'
            when is_closed_lost then 'CLOSED_LOST'
            else 'OPEN'
        end as lifecycle_status,
        created_at::timestamp_ntz as created_at,
        updated_at::timestamp_ntz as updated_at,
        _ingested_at::timestamp_ntz as _ingested_at,
        _batch_id::varchar as _batch_id
    from {{ source('raw', 'crm_opportunities') }}
)
select *
from source_opportunities
where opportunity_id is not null;
