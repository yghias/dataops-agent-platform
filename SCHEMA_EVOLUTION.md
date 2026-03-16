# Schema Evolution

## Supported change types

### Added columns
- preserve ingestion by landing the new column into raw storage
- allow staging models to ignore the new column until reviewed
- require contract update before canonical mart usage

### Renamed columns
- treat as breaking changes
- surface schema drift alerts
- block publication until mapping or upstream remediation is approved

### Type changes
- allow only widening changes without explicit review
- require staging coercion logic and validation before downstream publish

## Operational response

1. detect drift from registry or landed file inspection
2. classify drift type and impacted assets
3. route to Data Architect Agent plus Data Engineer Agent
4. generate proposed contract and SQL updates
5. require human review before publication

## Backward compatibility

- raw layer stores the full landed payload where feasible
- staging models apply deterministic coercion
- marts never silently change semantics based on upstream drift
