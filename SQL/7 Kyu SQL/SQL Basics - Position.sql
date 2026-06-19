/*  SQL  */
select m.id, 
      m.name,
      position(',' in m.characteristics) as comma
from monsters as m
order by comma