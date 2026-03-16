select
    source_system,
    entity_name,
    drift_type,
    date_trunc('day', effective_at) as effective_day,
    count(*) as drift_events
from {{ ref('stg_schema_versions') }}
where drift_type is not null
group by 1, 2, 3, 4;
