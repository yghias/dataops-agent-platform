with source_amounts as (
    select
        date_trunc('month', order_ts) as revenue_month,
        sum(gross_revenue) as source_revenue
    from analytics.orders
    group by 1
),
mart_amounts as (
    select
        revenue_month,
        sum(gross_revenue) as mart_revenue
    from analytics.mart_monthly_revenue
    group by 1
)
select
    s.revenue_month,
    s.source_revenue,
    m.mart_revenue
from source_amounts s
left join mart_amounts m
    on s.revenue_month = m.revenue_month
where coalesce(s.source_revenue, 0) <> coalesce(m.mart_revenue, 0);
