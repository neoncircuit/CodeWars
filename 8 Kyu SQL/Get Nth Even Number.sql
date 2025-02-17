-- # write your SQL statement here: you are given a table 'ntheven' with column 'n', return a table with column 'n' and your result in a column named 'res'.
select
  nth.n,
  ((nth.n*2) - 2) as res
from
  ntheven as nth