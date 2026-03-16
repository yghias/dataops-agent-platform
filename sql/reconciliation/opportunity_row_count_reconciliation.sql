with raw_counts as (
    select count(*) as raw_row_count
    from raw.crm.crm_opportunities
),
staging_counts as (
    select count(*) as staging_row_count
    from staging.stg_crm_opportunities
),
intermediate_counts as (
    select count(*) as intermediate_row_count
    from intermediate.int_opportunity_daily_snapshot
)
select
    raw_row_count,
    staging_row_count,
    intermediate_row_count
from raw_counts
cross join staging_counts
cross join intermediate_counts;
