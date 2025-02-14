/*  SQL  */
select d.*,
      ascii(left(d.name, 1)) as name,
      ascii(left(d.race, 1)) as race
from demographics as d