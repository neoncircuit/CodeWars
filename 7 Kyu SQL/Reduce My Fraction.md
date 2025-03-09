# Reduce My Fraction

## Instructions

Write a function which reduces fractions to their simplest form! Fractions will be presented as an array/tuple (depending on the language) of strictly positive integers, and the reduced fraction must be returned as an array/tuple:

```
input:   [numerator, denominator]
output:  [reduced numerator, reduced denominator]
example: [45, 120] --> [3, 8]
```

All numerators and denominators will be positive integers.

Note: This is an introductory Kata for a series... coming soon!

## Given Code
```sql
-- # write your SQL statement here: 
-- you are given a table 'fraction' with columns 'numerator' (int) and 'denominator' (int)
-- return a query with columns 'numerator', 'denominator', 'reduced_numerator' (int) and 'reduced_denominator' (int)
-- sort results by column 'numerator' ascending, then by 'denominator' ascending
```

## My Solution
```sql
-- # write your SQL statement here: 
-- you are given a table 'fraction' with columns 'numerator' (int) and 'denominator' (int)
-- return a query with columns 'numerator', 'denominator', 'reduced_numerator' (int) and 'reduced_denominator' (int)
-- sort results by column 'numerator' ascending, then by 'denominator' ascending
select 
  f.numerator,
  f.denominator,
  f.numerator/gcd(f.numerator, f.denominator) as reduced_numerator,
  f.denominator/gcd(f.numerator, f.denominator) as reduced_denominator
from 
  fraction as f
order by
  f.numerator, f.denominator asc
```
