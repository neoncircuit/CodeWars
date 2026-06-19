-- # write your SQL statement here: you are given a table 'nospace' with column 'x', return a table with column 'x' and your result in a column named 'res'.
select n.x,
      replace(n.x, ' ', '') as res
from nospace as n