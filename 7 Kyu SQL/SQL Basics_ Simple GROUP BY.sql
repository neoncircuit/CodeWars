-- Create your SELECT statement here
select age, count(*) as people_count 
from people
group by age