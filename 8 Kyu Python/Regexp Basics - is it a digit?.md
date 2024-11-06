# Regexp Basics - is it a digit?

## Instructions

Implement String#digit? (in Java StringUtils.isDigit(String)), which should return true if given object is a digit (0-9), false otherwise.

## Given Code
```python
def is_digit(n):
    #your code here
```

## My Solution
```python
import re

def is_digit(n):
    #your code here
    if re.fullmatch(r"[0-9]", n) and 0 <= int(n) < 10:
        return True
    else:
        return False
```