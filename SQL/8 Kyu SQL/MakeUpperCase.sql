--# write your SQL statement here: you are given a table 'makeuppercase' with column 's', return a table with column 's' and your uppercased result in a column named 'res'.
select m.s,
      upper(m.s) as res
from makeuppercase as m