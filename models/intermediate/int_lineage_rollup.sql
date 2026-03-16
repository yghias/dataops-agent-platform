select
    l.upstream_asset_id,
    u.asset_name as upstream_asset_name,
    l.downstream_asset_id,
    d.asset_name as downstream_asset_name,
    l.transform_layer,
    l.transform_name,
    l.created_at
from platform.table_lineage l
join {{ ref('stg_data_assets') }} u
    on l.upstream_asset_id = u.asset_id
join {{ ref('stg_data_assets') }} d
    on l.downstream_asset_id = d.asset_id;
