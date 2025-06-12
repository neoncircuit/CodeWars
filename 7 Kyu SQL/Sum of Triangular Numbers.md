# Sum of Triangular Numbers

## Instructions

Your task is to return the sum of Triangular Numbers up-to-and-including the nth Triangular Number.

Triangular Number: "any of the series of numbers (1, 3, 6, 10, 15, etc.) obtained by continued summation of the natural numbers 1, 2, 3, 4, 5, etc."

```
[01]
02 [03]
04 05 [06]
07 08 09 [10]
11 12 13 14 [15]
16 17 18 19 20 [21]
```

e.g. If 4 is given: `1 + 3 + 6 + 10 = 20`.

Triangular Numbers cannot be negative so return 0 if a negative number is given.

## Given Code
```
--# write your SQL statement here: 
-- you are given a table 'sumtriangular' with column 'n'
-- return a table with this column and your result in a column named 'res'.
```

## My Solution
```
--# write your SQL statement here: 
-- you are given a table 'sumtriangular' with column 'n'
-- return a table with this column and your result in a column named 'res'.
select
  s.n,
  case
    when s.n < 0 then 0
    else (s.n * (s.n + 1) * (s.n + 2)) / 6
  end as res
from
  sumtriangular as s
```