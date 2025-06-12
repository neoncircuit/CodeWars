-- # write your SQL statement here: 
-- you are given a table 'counter' with columns 'x' (int) and 'n' (int)
-- return a query with columns 'x', 'n' and your result in a column named 'res' (array)
-- sort results by column 'x' ascending, then by 'n' ascending
-- note that each pair of 'x' and 'n' in 'counter' is unique 
select
  c.x, 
  c.n,
  case
    when c.n = 0 then array[]::integer[]
    else array(select s.val * c.x from generate_series(1, c.n) as s(val))
  end as res
from
  counter as c
where
  c.n > 0
order by
  c.x asc, 
  c.n asc