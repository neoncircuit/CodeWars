# How do I compare numbers?

## Instructions

What could be easier than comparing integer numbers? However, the given piece of code doesn't recognize some of the special numbers for a reason to be found. Your task is to find the bug and eliminate it.



## Given Code
```python
def what_is(x):
    if x is 42:
        return 'everything'
    elif x is 42 * 42:
        return 'everything squared'
    else:
        return 'nothing'
```

## My Solution
```python
def what_is(x):
    if x == 42:
        return 'everything'
    elif x == 42 * 42:
        return 'everything squared'
    else:
        return 'nothing'
```
