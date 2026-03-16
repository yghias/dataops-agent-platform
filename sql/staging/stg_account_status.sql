select
    account_id,
    account_name,
    industry,
    region,
    account_owner_name,
    account_status,
    updated_at
from staging.stg_crm_accounts
where account_status in ('ACTIVE', 'PROSPECT');
