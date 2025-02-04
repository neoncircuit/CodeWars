/*  SQL  */
select d.id, d.name, d.birthday, lower(d.race) as race
from demographics as d