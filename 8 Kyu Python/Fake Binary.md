# Fake Binary

Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

Note: input will never be an empty string

# Given Code

```{python}
def fake_bin(x):
    pass
```

# My Solution

```{python}
def fake_bin(x):
    res = ""
    for i in x:
        if i >= '5':
            res += '1'
        else:
            res += '0'
    return res
```
