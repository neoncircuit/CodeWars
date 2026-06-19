--# write your SQL statement here: 
-- you are given a table 'squares' with column 'n' (number of cubes).
-- return a table with:
--   this column and your result in a column named 'res'
select s.n,
      case 
        when s.n = 0 then 1
        else cast(8 + 12 * (s.n - 1) + 6 * power(s.n - 1, 2) as int)
      end as res
from squares as s