-- required columns must be present for crm opportunities contract
select schema_version_id
from platform.schema_versions
where source_system = 'crm'
  and entity_name = 'opportunities'
  and not (
      array_contains('opportunity_id'::variant, schema_payload:"columns")
      and array_contains('account_id'::variant, schema_payload:"columns")
      and array_contains('amount'::variant, schema_payload:"columns")
  );

-- contract rows must be active for the latest schema version
select source_system, entity_name
from platform.data_contracts
qualify row_number() over (
    partition by source_system, entity_name
    order by version_number desc
) = 1
and status <> 'active';
