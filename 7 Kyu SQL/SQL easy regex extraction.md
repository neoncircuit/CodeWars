# SQL easy regex extraction

## Instructions

## Input

You'll have a table like the following:

| name | greeting |
| ----------- | ----------- |
| Austin Gaylord | Hola que tal #4702665|
| Kacie Zulauf | Bienvenido 45454545 tal #470815 BD. WA470815|

## Output

In this practice you'll need to extract from the greeting column the number preceeded by the `#` symbol and place it in a new column named `user_id`.

| name | greeting | user_id |
| ----------- | ----------- | ----------- |
| Austin Gaylord | Hola que tal #4702665 | 4702665 |
| Kacie Zulauf | Bienvenido 45454545 tal #470815 BD. WA470815 | 470815 |

NOTE: To keep it simple assume that the user_id will be having varchar type

## Given Code
```sql
SELECT * FROM greetings;
```

## My Solution
```sql
select 
  g.name,
  g.greeting,
  substring(greeting from '#(\d+)') as user_id
from 
  greetings as g
```
