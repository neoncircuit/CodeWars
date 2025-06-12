-- # write your SQL statement here: you are given a table 'paperwork' with columns 'id', 'n' and 'm', return a table with columns 'n', 'm' and your result in a column named 'res'.
select
  p.n,
  p.m,
  case 
    when p.n < 0 or p.m < 0 then 0
    else p.n * p.m
  end as res
from
  paperwork as p