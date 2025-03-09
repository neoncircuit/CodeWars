-- # write your SQL statement here: 
-- you are given a table 'fraction' with columns 'numerator' (int) and 'denominator' (int)
-- return a query with columns 'numerator', 'denominator', 'reduced_numerator' (int) and 'reduced_denominator' (int)
-- sort results by column 'numerator' ascending, then by 'denominator' ascending
select 
  f.numerator,
  f.denominator,
  f.numerator/gcd(f.numerator, f.denominator) as reduced_numerator,
  f.denominator/gcd(f.numerator, f.denominator) as reduced_denominator
from 
  fraction as f
order by
  f.numerator, f.denominator asc