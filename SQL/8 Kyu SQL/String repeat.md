# String repeat

## Instructions

Write a function that accepts a non-negative integer n and a string s as parameters, and returns a string of s repeated exactly n times.

## Examples (input -> output)

```
6, "I"     -> "IIIIII"
5, "Hello" -> "HelloHelloHelloHelloHello"
```

## Given Code
```sql
--# write your SQL statement here: you are given a table 'repeatstr' with columns 'n' and 's', return a table with all columns and your result in a column named 'res'.
```

## My Solution
```sql
--# write your SQL statement here: you are given a table 'repeatstr' with columns 'n' and 's', return a table with all columns and your result in a column named 'res'.
select
  r.s,
  r.n,
  repeat(r.s, r.n) as res
from 
  repeatstr as r
```
