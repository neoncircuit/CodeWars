# Simple validation of a username with regex

## Instructions

Write a simple regex to validate a username. Allowed characters are:

- lowercase letters,
- numbers,
- underscore

Length should be between 4 and 16 characters (both included).

## Given Code
```python
def validate_usr(username):
    #your code here
```

## My Solution
```python
import re

def validate_usr(username):
    #your code here
    return bool(re.fullmatch(r"[a-z0-9_]{4,16}", username))

```
