# SQL Basics: Maths with String Manipulations

## Instructions

Given a demographics table in the following format:

## demographics table schema

- id

- name

- birthday

- race

return a single column named `calculation` where the value is the bit length of name, added to the number of characters in race.

## Given Code
```sql
/*  SQL  */
```

## My Solution
```sql
/*  SQL  */
select 
  bit_length(d.name) + char_length(d.race) as calculation
from
  demographics as d
```
