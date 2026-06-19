/*  SQL  */
select
  d.race,
  count(d.id) as count
from
  demographics as d
group by 
  d.race
order by 
  count desc