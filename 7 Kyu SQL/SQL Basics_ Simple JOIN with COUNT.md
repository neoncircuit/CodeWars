# SQL Basics: Simple JOIN with COUNT

## Instructions

For this challenge you need to create a simple SELECT statement that will return all columns from the people table, and join to the toys table so that you can return the COUNT of the toys

## people table schema

- id

- name

## toys table schema

- id

- name

- people_id

You should return all people fields as well as the toy count as "toy_count".

NOTE: Your solution should use pure SQL. Ruby is used within the test cases to do the actual testing.

## Given Code
```sql
-- Create your SELECT statement here
```

## My Solution
```sql
-- Create your SELECT statement here
select 
  p.id,
  p.name,
  count(t.id) as toy_count
from 
  people as p
left join 
  toys as t on p.id = t.people_id
group by 
  p.id, p.name
```
