# If you can't sleep, just count sheep!!

If you can't sleep, just count sheep!!

## Task:

Given a non-negative integer, 3 for example, return a string with a murmur: 

```"1 sheep...2 sheep...3 sheep..."```. 

Input will always be valid, i.e. no negative integers.

# Given Code

```{python}
def count_sheep(n):
    # your code
```

# My Solution

```{python}
def count_sheep(n):
    murmur = ""
    for i in range(1, n+1):
        murmur += str(i) + " sheep..."
    return murmur
```
