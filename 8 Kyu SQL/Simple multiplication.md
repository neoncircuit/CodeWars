# Simple multiplication

## Instructions

This kata is about multiplying a given number by eight if it is an even number and by nine otherwise.

## Given Code
```
-- # write your SQL statement here: you are given a table 'multiplication' with column 'number', return a table with column 'number' and your result in a column named 'res'.
```

## My Solution
```
-- # write your SQL statement here: you are given a table 'multiplication' with column 'number', return a table with column 'number' and your result in a column named 'res'.
select
  m.number,
  case
    when m.number % 2 = 0 then m.number * 8
    else m.number * 9
  end as res
from
  multiplication as m
```