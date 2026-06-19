# Remove exclamation marks

## Instructions

Write function RemoveExclamationMarks which removes all exclamation marks from a given string.

## Given Code
```
-- # write your SQL statement here: you are given a table 'removeexclamationmarks' with column 's', return a table with column 's' and your result in a column named 'res'.
```

## My Solution
```
-- # write your SQL statement here: you are given a table 'removeexclamationmarks' with column 's', return a table with column 's' and your result in a column named '
select
  r.s,
  replace(r.s, '!', '') as res
from 
  removeexclamationmarks as r
```