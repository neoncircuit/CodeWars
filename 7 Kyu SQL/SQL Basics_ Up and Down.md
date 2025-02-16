# SQL Basics: Up and Down

## Instructions

Given a table of random numbers as follows:

## numbers table schema

- id

- number1

- number2

Your job is to return table with similar structure and headings, where if the sum of a column is odd, the column shows the minimum value for that column, and when the sum is even, it shows the max value. You must use a case statement.

## output table schema

- number1

- number2

## Given Code
```sql
/*  SQL  */
```

## My Solution
```sql
/*  SQL  */
select
  case 
    when sum(n.number1) % 2 = 1 then min(n.number1)
    else max(n.number1)
  end as number1,
  case 
    when sum(n.number2) % 2 = 1 then min(n.number2)
    else max(n.number2)
  end as number2
from
  numbers as n
```
