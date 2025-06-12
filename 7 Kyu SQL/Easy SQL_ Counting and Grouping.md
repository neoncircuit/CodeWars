# Easy SQL: Counting and Grouping

## Instructions

Given a demographics table in the following format:

**demographics table schema**

- id
- name
- birthday
- race

you need to return a table that shows a count of each race represented, ordered by the count in descending order as:

**output table schema**

- race
- count

## Given Code
```
/*  SQL  */
```

## My Solution
```
/*  SQL  */
select
  d.race,
  count(d.id) as count
from
  demographics as d
group by 
  d.race
order by 
  count desc
```