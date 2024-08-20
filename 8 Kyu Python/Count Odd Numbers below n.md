# Count Odd Numbers below n

Given a number n, return the number of positive odd numbers below n, EASY!

## Examples (Input -> Output)
7  -> 3 (because odd numbers below 7 are [1, 3, 5])
15 -> 7 (because odd numbers below 15 are [1, 3, 5, 7, 9, 11, 13])

Expect large Inputs!

# Given Code

```{python}
def odd_count(n):
    pass
```

# My Solution

```{python}
def odd_count(n):
    odd = []
    for i in range(n):
        if i % 2 != 0:
            odd.append(i)
    return len(odd)
```
