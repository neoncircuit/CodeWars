# Count the number of cubes with paint on

## Instructions

Upon arriving at an interview, you are presented with a solid blue cube. The cube is then dipped in red paint, coating the entire surface of the cube. The interviewer then proceeds to cut through the cube in all three dimensions a certain number of times.

Your function takes as parameter the number of times the cube has been cut. You must return the number of smaller cubes created by the cuts that have at least one red face.

To make it clearer, the picture below represents the cube after (from left to right) 0, 1 and 2 cuts have been made.

![alt text](https://i.imgur.com/36x8Fkv.png)

## Given Code
```sql
--# write your SQL statement here: 
-- you are given a table 'squares' with column 'n' (numer of cubes).
-- return a table with:
--   this column and your result in a column named 'res'
```

## My Solution
```sql
--# write your SQL statement here: 
-- you are given a table 'squares' with column 'n' (number of cubes).
-- return a table with:
--   this column and your result in a column named 'res'
select s.n,
      case 
        when s.n = 0 then 1
        else cast(8 + 12 * (s.n - 1) + 6 * power(s.n - 1, 2) as int)
      end as res
from squares as s
```
