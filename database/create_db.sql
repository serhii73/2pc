CREATE TABLE IF NOT EXISTS flybooking (
    name TEXT,
    flyNumber TEXT,
    fromPlace TEXT,
    toPlace TEXT,
    dateFly DATE
);

CREATE TABLE IF NOT EXISTS hotelbooking (
    name TEXT,
    hotelName TEXT,
    Arrival DATE,
    Departure DATE
);

CREATE TABLE IF NOT EXISTS account (
    name TEXT,
    amount NUMERIC(15,6)
);


-- drop table if exists dim_customer;
-- create table dim_customer(
--     customer_sk serial primary key,
--     customer_bk varchar(255),
--     full_name  varchar(255),   -- SCD1 attribure
--     country varchar(255),      -- SCD2 attribure
--     state_region varchar(255), -- SCD2 attribure
--     valid_from timestamp,
--     valid_to timestamp
-- );
