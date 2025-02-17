# Even or Odd

## Instructions

You will be given a table `numbers`, with one column `number`.

Return a dataset with two columns: `number` and `is_even`, where `number` contains the original input value, and `is_even` containing `"Even"` or `"Odd"` depending on `number` column values.

## Numbers table schema

```
* number INT
```

## Output table schema

```
* number  INT
* is_even STRING
```

## Given Code
```sql
--# write your SQL SELECT statement here: you are given a table 'numbers' with column 'number', return a table with column 'number' and your result in a column named 'is_even'.
```

## My Solution
```sql
--# write your SQL SELECT statement here: you are given a table 'numbers' with column 'number', return a table with column 'number' and your result in a column named 'is_even'.
select
  n.number,
  case
    when n.number % 2 = 0 then 'Even'
    else 'Odd'
  end as is_even
from
  numbers as n
```
