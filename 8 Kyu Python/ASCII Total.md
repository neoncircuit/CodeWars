# ASCII Total

## Instructions

You'll be given a string, and have to return the sum of all characters as an int. The function should be able to handle all printable ASCII characters.

Examples:

```
uniTotal("a") == 97
uniTotal("aaa") == 291
```

## Given Code
```python
def uni_total(s):
    pass
```

## My Solution
```python
def uni_total(s):
    return sum(ord(char) for char in s)
```
