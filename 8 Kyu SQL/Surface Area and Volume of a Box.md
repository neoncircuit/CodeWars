# Surface Area and Volume of a Box

## Instructions

You are given a table 'box' with columns: width (int), height (int), depth (int). Write a query that returns these columns: width, height, depth, area (int), volume (int). Sort results by area ascending, then volume ascending, then width ascending, then height ascending

## Given Code
```sql
-- # write your SQL statement here: 
-- you are given a table 'box' with columns: width (int), height (int), depth (int)
-- return a query with columns: width, height, depth, area (int), volume (int)
-- sort results by area ascending, then volume ascending, then width ascending, then height ascending
```

## My Solution
```sql
-- # write your SQL statement here: 
-- you are given a table 'box' with columns: width (int), height (int), depth (int)
-- return a query with columns: width, height, depth, area (int), volume (int)
-- sort results by area ascending, then volume ascending, then width ascending, then height ascending
select
  b.width,
  b.height,
  b.depth,
  ((2*b.depth*b.width) + (2*b.depth*b.height) + (2*b.height*b.width)) as area,
  (b.width * b.height * b.depth) as volume
from
  box as b
order by
  area, 
  volume, 
  b.width, 
  b.height asc
```
