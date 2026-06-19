# Function 2 - squaring an argument

## Instructions

Now you have to write a function that takes an argument and returns the square of it.

## Given Code
```
--# write your SQL statement here: 
-- you are given a table 'square' with column 'n'
-- return a table with:
--   this column and your result in a column named 'res'
```

## My Solution
```
--# write your SQL statement here: 
-- you are given a table 'square' with column 'n'
-- return a table with:
--   this column and your result in a column named 'res'
select 
  s.n,
  power(s.n, 2)::integer as res
from
  square as s;
```