# Easy SQL: LowerCase

## Instructions

Given a demographics table in the following format:

## demographics table schema 

- id

- name

- birthday

- race

you need to return the same table where all letters are lowercase in the race column.

## Given Code
```sql
/*  SQL  */
```

## My Solution
```sql
/*  SQL  */
select d.id, d.name, d.birthday, lower(d.race) as race
from demographics as d
```
