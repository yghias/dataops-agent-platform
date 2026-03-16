create or replace view analytics.mart_monthly_revenue as
select
    date_trunc('month', order_ts) as revenue_month,
    customer_id,
    count(*) as order_count,
    sum(gross_revenue) as gross_revenue,
    sum(discount_amount) as discount_amount
from analytics.orders
group by 1, 2;

create or replace view analytics.mart_customer_lifetime_value as
select
    c.customer_id,
    c.customer_name,
    min(o.order_ts) as first_order_ts,
    max(o.order_ts) as latest_order_ts,
    count(o.order_id) as lifetime_orders,
    sum(o.gross_revenue) as lifetime_revenue
from analytics.customers c
left join analytics.orders o
    on c.customer_id = o.customer_id
group by 1, 2;
