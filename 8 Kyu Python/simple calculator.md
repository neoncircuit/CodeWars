# simple calculator

## Instructions

You are required to create a simple calculator that returns the result of addition, subtraction, multiplication or division of two numbers.

Your function will accept three arguments:
The first and second argument should be numbers.
The third argument should represent a sign indicating the operation to perform on these two numbers.

if the variables are not numbers or the sign does not belong to the list above a message "unknown value" must be returned.

## Example:

```
calculator(1, 2, '+') => 3
calculator(1, 2, '$') # result will be "unknown value"
```

Good luck!

## Given Code
```python
def calculator(x,y,op):
    pass
```

## My Solution
```python
def calculator(x,y,op):
    while type(x) == int and type(y) == int and type(op) == str and op in {"+", "-", "/", "*"}:
        return eval(f"{x} {op} {y}")
        break
    return "unknown value"
```
