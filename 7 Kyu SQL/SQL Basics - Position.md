# SQL Basics - Position

## Instructions

You have access to a table of monsters as follows:

## monsters schema

- id

- name

- legs

- arms

- characteristics

In each row, the characteristic column has a single comma. Your job is to find it using position(). You must return a table with the format as follows:

## output schema

- id

- name

- comma

The comma column will contain the position of the comma within the characteristics string. Order the results by comma.

## Given Code
```sql
/*  SQL  */
```

## My Solution
```sql
/*  SQL  */
select m.id, 
      m.name,
      position(',' in m.characteristics) as comma
from monsters as m
order by comma
```
