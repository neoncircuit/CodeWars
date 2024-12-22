# String Templates - Bug Fixing #5

## Instructions

Oh no! Timmy hasn't followed instructions very carefully and forgot how to use the new String Template feature, Help Timmy with his string template so it works as he expects!

## Given Code
```python
def build_string(*args):
    return "I like {1}!".format(",".join(args))
```

## My Solution
```python
def build_string(*args):
    return "I like {}!".format(", ".join(args))
```
