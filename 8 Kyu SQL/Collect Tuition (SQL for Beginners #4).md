# Collect Tuition (SQL for Beginners #4)

## Instructions

You are working for a local school, and you are responsible for collecting tuition from students. You have a list of all students, some of them have already paid tution and some haven't. Write a select statement to get a list of all students who haven't paid their tuition yet. The list should include all the data available about these students.

students table schema

- name (string)

- age (integer)

- semester (integer)

- mentor (string)

- tuition_received (Boolean)

NOTE: Your solution should use pure SQL. Ruby is used within the test cases just to validate your answer.

## Given Code
```sql
-- Your Code Here
```

## My Solution
```sql
-- Your Code Here
select * from students
where not tuition_received
```
