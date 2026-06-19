--# write your SQL SELECT statement here: you are given a table 'numbers' with column 'number', return a table with column 'number' and your result in a column named 'is_even'.
select
  n.number,
  case
    when n.number % 2 = 0 then 'Even'
    else 'Odd'
  end as is_even
from
  numbers as n