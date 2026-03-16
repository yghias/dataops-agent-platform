create schema if not exists analytics;

create table if not exists analytics.customers (
    customer_id bigint primary key,
    customer_name varchar(255) not null,
    customer_segment varchar(100),
    created_at timestamp not null,
    updated_at timestamp not null
);

create table if not exists analytics.orders (
    order_id bigint primary key,
    customer_id bigint not null references analytics.customers(customer_id),
    order_ts timestamp not null,
    order_status varchar(50) not null,
    gross_revenue numeric(18,2) not null,
    discount_amount numeric(18,2) default 0,
    load_date date not null
);

create table if not exists analytics.customer_activity (
    activity_id bigint primary key,
    customer_id bigint not null references analytics.customers(customer_id),
    activity_date date not null,
    activity_type varchar(100) not null,
    activity_flag boolean not null default true
);
