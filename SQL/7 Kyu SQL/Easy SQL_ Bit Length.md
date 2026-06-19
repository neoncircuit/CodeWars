# Easy SQL: Bit Length

## Instructions

Given a demographics table in the following format:

## demographics table schema 

- id

- name

- birthday

- race

you need to return the same table where all text fields (name & race) are changed to the bit length of the string.

## Given Code
```sql
/*  SQL  */
```

## My Solution
```sql
/*  SQL  */
select d.*,
      bit_length(d.name) as name,
      bit_length(d.race) as race
from demographics as d
```
