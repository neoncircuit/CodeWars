# MakeUpperCase

## Instructions

Write a function which converts the input string to uppercase.

## Given Code
```sql
--# write your SQL statement here: you are given a table 'makeuppercase' with column 's', return a table with column 's' and your uppercased result in a column named 'res'.
```

## My Solution
```sql
--# write your SQL statement here: you are given a table 'makeuppercase' with column 's', return a table with column 's' and your uppercased result in a column named 'res'.
select m.s,
      upper(m.s) as res
from makeuppercase as m
```
