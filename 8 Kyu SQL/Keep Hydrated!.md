# Keep Hydrated!

## Instructions

Nathan loves cycling.

Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.

You get given the time in hours and you need to return the number of litres Nathan will drink, rounded to the smallest value.

For example:

```
hours = 3 ----> liters = 1

hours = 6.7---> liters = 3

hours = 11.8--> liters = 5
```

Input data is available from the table `cycling`, which has 2 columns: `id` and `hours`. For each row, you have to return 3 columns: `id`, `hours` and `liters` (not litres, it's a difference from the kata description)

## Given Code
```sql
SELECT * FROM cycling
```

## My Solution
```sql
select
  c.id,
  c.hours,
  (floor(c.hours/2)) as liters
from
  cycling as c
```
