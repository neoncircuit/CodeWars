-- # write your SQL statement here: you are given a table 'multiplication' with column 'number', return a table with column 'number' and your result in a column named 'res'.
select
  m.number,
  case
    when m.number % 2 = 0 then m.number * 8
    else m.number * 9
  end as res
from
  multiplication as m