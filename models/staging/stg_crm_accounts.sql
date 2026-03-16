with source_accounts as (
    select
        account_id::varchar as account_id,
        trim(account_name)::varchar as account_name,
        upper(trim(industry))::varchar as industry,
        trim(region)::varchar as region,
        owner_name::varchar as account_owner_name,
        status::varchar as account_status,
        created_at::timestamp_ntz as created_at,
        updated_at::timestamp_ntz as updated_at,
        _ingested_at::timestamp_ntz as _ingested_at,
        _batch_id::varchar as _batch_id
    from {{ source('raw', 'crm_accounts') }}
)
select *
from source_accounts
where account_id is not null;
