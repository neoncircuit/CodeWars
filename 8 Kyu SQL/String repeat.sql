--# write your SQL statement here: you are given a table 'repeatstr' with columns 'n' and 's', return a table with all columns and your result in a column named 'res'.
select
  r.s,
  r.n,
  repeat(r.s, r.n) as res
from 
  repeatstr as r