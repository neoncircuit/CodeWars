# Drink about

## Instructions

- Kids drink toddy.
- Teens drink coke.
- Young adults drink beer.
- Adults drink whisky.

Make a function that receive age, and return what they drink.

## Rules:

- Children under 14 old.
- Teens under 18 old.
- Young under 21 old.
- Adults have 21 or more.

## Examples: (Input --> Output)

```
13 --> "drink toddy"
17 --> "drink coke"
18 --> "drink beer"
20 --> "drink beer"
30 --> "drink whisky"
```

## Given Code
```python
def people_with_age_drink(age):
    return ''
```

## My Solution
```python
def people_with_age_drink(age):
    return "drink toddy" if age < 14 else "drink coke" if age < 18 else "drink beer" if age < 21 else "drink whisky"
```