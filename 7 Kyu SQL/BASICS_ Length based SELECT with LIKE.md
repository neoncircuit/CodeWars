# BASICS: Length based SELECT with LIKE

## Instructions

You will need to create SELECT statement in conjunction with LIKE.

Please list people which have first_name with at least 6 character long

## names table schema

- id

- first_name

- last_name

## results table schema

- first_name

- last_name

## Given Code
```sql
-- Replace with your SQL Query
```

## My Solution
```sql
-- Replace with your SQL Query
select n.first_name, 
      n.last_name
from names as n
where n.first_name like '______%'
```
