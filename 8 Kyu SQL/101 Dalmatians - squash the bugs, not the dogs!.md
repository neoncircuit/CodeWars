# 101 Dalmatians - squash the bugs, not the dogs!

## Instructions

Your friend has been out shopping for puppies (what a time to be alive!)... He arrives back with multiple dogs, and you simply do not know how to respond!

By repairing the function provided, you will find out exactly how you should respond, depending on the number of dogs he has.

The number of dogs will always be a number and there will always be at least 1 dog.

```
Good luck!
```

## Given Code
```sql
-- # write your SQL statement here: 
-- you are given a table 'dalmatians' with column 'n' (int)
-- return a query with column 'n' and your result in a column named 'res' (text)
-- sort results by column 'n' ascending

select n, switch case
  when n <= 10 then do 'Hardly any' end
  when n <= 50 then do 'More than a handful!' end
  when n == 101 then do '101 DALMATIONS!!!' end
  else do 'Woah that''s a lot of dogs!' end switch as res
from dalmatians
order by 1 asc;
```

## My Solution
```sql
-- # write your SQL statement here: 
-- you are given a table 'dalmatians' with column 'n' (int)
-- return a query with column 'n' and your result in a column named 'res' (text)
-- sort results by column 'n' ascending

select 
  d.n,
  case 
    when d.n <= 10 then 'Hardly any'
    when d.n <= 50 then 'More than a handful!'
    when d.n = 101 then '101 DALMATIANS!!!'
    else 'Woah that''s a lot of dogs!' 
  end as res
from
  dalmatians as d
order by 
  d.n asc
```
