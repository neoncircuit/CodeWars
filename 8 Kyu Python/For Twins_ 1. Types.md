# For Twins: 1. Types

## Instructions

## Prolog:

This kata series was created for friends of mine who just started to learn programming. Wish you all the best and keep your mind open and sharp!

## Task:

Write a function that will accept two parameters: variable and type and check if type of variable is matching type. Return true if types match or false if not.

## Examples:

```
42, "int"    --> True
"42", "int"  --> False
```

## Given Code
```python
def type_validation(variable, _type): 
    # your code here
    pass
```

## My Solution
```python
def type_validation(variable, _type): 
    # your code here
    return type(variable).__name__ == _type
```
