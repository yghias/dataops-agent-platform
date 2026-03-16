select
    quality_result_id,
    run_id,
    asset_id,
    check_name,
    check_type,
    measured_value::number(18,4) as measured_value,
    threshold_value::number(18,4) as threshold_value,
    status,
    measured_at::timestamp_ntz as measured_at
from platform.data_quality_results;
