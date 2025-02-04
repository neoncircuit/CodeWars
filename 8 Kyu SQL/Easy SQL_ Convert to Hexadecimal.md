# Easy SQL: Convert to Hexadecimal

## Instructions

to hexYou have access to a table of monsters as follows:

## monsters table schema

- id

- name

- legs

- arms

- characteristics

Your task is to turn the numeric columns (`arms`, `legs`) into equivalent hexadecimal values.

## output table schema

- legs

- arms

## Given Code
```sql
/*  SQL  */
```

## My Solution
```sql
/*  SQL  */
select to_hex(m.legs) as legs, to_hex(m.arms) as arms
from monsters as m
```
