select c.id,
      text(network(c.ip_address)) as first_address,
      text(broadcast(c.ip_address)) as last_address
from connections as c
order by c.id