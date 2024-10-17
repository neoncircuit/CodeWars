# Ensure question

## Instructions

Given a string, write a function that returns the string with a question mark ("?") appends to the end, unless the original string ends with a question mark, in which case, returns the original string.

## For example (Input --> Output)

```
"Yes" --> "Yes?" 
"No?" --> "No?"
```

## Given Code
```python
def ensure_question(s):
    # Code here
```

## My Solution
```python
def ensure_question(s):
    # Code here
    if s.endswith("?"):
        return s
    else:
        return s + "?"
```
