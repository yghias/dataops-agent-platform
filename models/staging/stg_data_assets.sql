select
    asset_id,
    asset_name,
    asset_type,
    domain_name,
    owner_role,
    sensitivity_class,
    sla_minutes::number(10,0) as sla_minutes,
    created_at::timestamp_ntz as created_at,
    updated_at::timestamp_ntz as updated_at
from platform.data_assets;
