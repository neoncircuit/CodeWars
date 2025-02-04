# Easy SQL: Square Root and Log

## Instructions

Given the following table 'decimals':

## decimals table schema 

- id

- number1

- number2

Return a table with two columns (root, log) where the values in root are the square root of those provided in number1 and the values in log are changed to a base 10 logarithm from those in number2.

## Given Code
```sql
/* SQL */
```

## My Solution
```sql
/* SQL */
select sqrt(d.number1) as root, 
       log10(d.number2) as log
from decimals as d
```
