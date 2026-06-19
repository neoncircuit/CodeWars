# GROCERY STORE: Support Local Products

## Instructions

You are the owner of the Grocery Store. All your products are in the database, that you have created after CodeWars SQL excercises!:)

You care about local market, and want to check how many products come from United States of America or Canada.

Please use SELECT statement and IN to filter out other origins.

In the results show how many products are from United States of America and Canada respectively.

Order by number of products, descending.

**products table schema**
- id
- name
- price
- stock
- producer
- country

**results table schema**
- products
- country

## Given Code
```
-- Replace with your SQL Query
```

## My Solution
```
-- Replace with your SQL Query
select 
  count(p.id) as products,
  p.country
from 
  products as p
where
  p.country in ('United States of America', 'Canada')
group by 
  p.country
order by
  products desc
```