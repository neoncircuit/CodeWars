/*  SQL  */
select left(r.project, r.commits) as project,
      right(r.address, r.contributors) as address
from repositories as r