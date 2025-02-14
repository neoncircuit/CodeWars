-- Substitute with your SQL
select b.book_id,
      b.title
from books as b
left join loans as l on b.book_id = l.book_id
group by b.book_id, b.title
having count(*) = count(l.return_date)
order by b.book_id desc