-- # write your SQL statement here: 
-- you are given a table 'box' with columns: width (int), height (int), depth (int)
-- return a query with columns: width, height, depth, area (int), volume (int)
-- sort results by area ascending, then volume ascending, then width ascending, then height ascending
select
  b.width,
  b.height,
  b.depth,
  ((2*b.depth*b.width) + (2*b.depth*b.height) + (2*b.height*b.width)) as area,
  (b.width * b.height * b.depth) as volume
from
  box as b
order by
  area, 
  volume, 
  b.width, 
  b.height asc