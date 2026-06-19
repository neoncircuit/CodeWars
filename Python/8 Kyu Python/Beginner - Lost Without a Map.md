# Beginner - Lost Without a Map

Given an array of integers, return a new array with each value doubled.

For example:

[1, 2, 3] --> [2, 4, 6]

# Given Code

```{python}
def maps(a):
    pass
```

# My Solution

```{python}
def maps(a):
    def double(n):
        return n*2
    
    return list(map(double, a))
```
