/*  SQL  */
select
  case 
    when sum(n.number1) % 2 = 1 then min(n.number1)
    else max(n.number1)
  end as number1,
  case 
    when sum(n.number2) % 2 = 1 then min(n.number2)
    else max(n.number2)
  end as number2
from
  numbers as n