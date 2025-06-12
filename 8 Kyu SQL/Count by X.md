# Count by X

## Instructions

Create a function with two arguments that will return an array of the first `n` multiples of `x`.

Assume both the given number and the number of times to count will be positive numbers greater than `0`.

Return the results as an array or list ( depending on language ).

## Examples
```
x = 1, n = 10 --> [1,2,3,4,5,6,7,8,9,10]
x = 2, n = 5  --> [2,4,6,8,10]
```

## Given Code
```
-- # write your SQL statement here: 
-- you are given a table 'counter' with columns 'x' (int) and 'n' (int)
-- return a query with columns 'x', 'n' and your result in a column named 'res' (array)
-- sort results by column 'x' ascending, then by 'n' ascending
-- note that each pair of 'x' and 'n' in 'counter' is unique
```

## My Solution
```
-- # write your SQL statement here: 
-- you are given a table 'counter' with columns 'x' (int) and 'n' (int)
-- return a query with columns 'x', 'n' and your result in a column named 'res' (array)
-- sort results by column 'x' ascending, then by 'n' ascending
-- note that each pair of 'x' and 'n' in 'counter' is unique 
select
  c.x, 
  c.n,
  case
    when c.n = 0 then array[]::integer[]
    else array(select s.val * c.x from generate_series(1, c.n) as s(val))
  end as res
from
  counter as c
where
  c.n > 0
order by
  c.x asc, 
  c.n asc
```