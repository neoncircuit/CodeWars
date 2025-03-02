-- Substitute with your SQL
select 
  c.id as customer_id,
  case
    when c.age between 18 and 65 
      and coalesce(max(l.loan_status), 'paid') = 'paid'
    then 'loan can be given'
    else 'loan cannot be given'
  end as loan_eligibility
from 
  customers as c
left join
  loans as l on c.id = l.customer_id
where
  c.id between 1 and 10
group by
  c.id, c.age
order by
  c.id desc