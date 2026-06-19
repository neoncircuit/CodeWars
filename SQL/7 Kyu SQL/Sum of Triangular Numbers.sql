--# write your SQL statement here: 
-- you are given a table 'sumtriangular' with column 'n'
-- return a table with this column and your result in a column named 'res'.
select
  s.n,
  case
    when s.n < 0 then 0
    else (s.n * (s.n + 1) * (s.n + 2)) / 6
  end as res
from
  sumtriangular as s