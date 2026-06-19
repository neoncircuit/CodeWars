select
  c.id,
  c.hours,
  (floor(c.hours/2)) as liters
from
  cycling as c