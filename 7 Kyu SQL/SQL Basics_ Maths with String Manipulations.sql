/*  SQL  */
select 
  bit_length(d.name) + char_length(d.race) as calculation
from
  demographics as d