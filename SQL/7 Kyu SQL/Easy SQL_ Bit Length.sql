/*  SQL  */
select d.*,
      bit_length(d.name) as name,
      bit_length(d.race) as race
from demographics as d