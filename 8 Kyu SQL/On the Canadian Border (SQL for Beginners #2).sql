--Your Code Here
select name, country 
from travelers
where country not in ('USA', 'Mexico', 'Canada')