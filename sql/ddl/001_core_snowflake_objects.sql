create schema if not exists raw.crm;
create schema if not exists staging;
create schema if not exists intermediate;
create schema if not exists analytics;

create or replace table raw.crm.crm_accounts (
    account_id varchar not null,
    account_name varchar,
    industry varchar,
    region varchar,
    owner_name varchar,
    status varchar,
    created_at timestamp_ntz,
    updated_at timestamp_ntz,
    _ingested_at timestamp_ntz not null,
    _batch_id varchar not null
);

create or replace table raw.crm.crm_opportunities (
    opportunity_id varchar not null,
    account_id varchar not null,
    owner_name varchar,
    stage_name varchar,
    amount number(18,2),
    probability number(5,2),
    expected_close_date date,
    close_date date,
    is_closed_won boolean,
    is_closed_lost boolean,
    created_at timestamp_ntz,
    updated_at timestamp_ntz,
    _ingested_at timestamp_ntz not null,
    _batch_id varchar not null
);
