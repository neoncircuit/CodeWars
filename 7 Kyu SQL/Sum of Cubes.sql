-- # write your SQL statement here: 
-- you are given a table 'cubes' with column 'n' (bigint)
-- return a query with column 'n' and your result in a column named 'res' (bigint)
-- sort results by column 'n' ascending
select c.*,
      cast((select sum(power(x, 3)) from generate_series(1, c.n) as x) as bigint) as res
from cubes as c
order by c.n asc