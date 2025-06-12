-- Replace with your SQL Query
select 
  count(p.id) as products,
  p.country
from 
  products as p
where
  p.country in ('United States of America', 'Canada')
group by 
  p.country
order by
  products desc