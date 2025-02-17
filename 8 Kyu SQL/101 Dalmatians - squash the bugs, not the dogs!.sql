-- # write your SQL statement here: 
-- you are given a table 'dalmatians' with column 'n' (int)
-- return a query with column 'n' and your result in a column named 'res' (text)
-- sort results by column 'n' ascending

select 
  d.n,
  case 
    when d.n <= 10 then 'Hardly any'
    when d.n <= 50 then 'More than a handful!'
    when d.n = 101 then '101 DALMATIANS!!!'
    else 'Woah that''s a lot of dogs!' 
  end as res
from
  dalmatians as d
order by 
  d.n asc