-- not null checks
select count(*) as null_customer_id_count
from analytics.orders
where customer_id is null;

-- referential integrity check
select count(*) as orphan_order_count
from analytics.orders o
left join analytics.customers c
    on o.customer_id = c.customer_id
where c.customer_id is null;

-- freshness check
select max(load_date) as latest_load_date
from analytics.orders;
