select
    schema_version_id,
    source_system,
    entity_name,
    version_number::number(10,0) as version_number,
    schema_payload,
    drift_type,
    effective_at::timestamp_ntz as effective_at
from platform.schema_versions;
