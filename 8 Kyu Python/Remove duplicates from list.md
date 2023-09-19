# Remove duplicates from list

Define a function that removes duplicates from an array of non negative numbers and returns it as a result.

The order of the sequence has to stay the same.

## Examples:

Input -> Output
[1, 1, 2] -> [1, 2]
[1, 2, 1, 1, 3, 2] -> [1, 2, 3]


# Given Code

```{python}
def distinct(seq):
    pass
```

# My Solution

```{python}
def distinct(seq):
    x = []
    for i in seq:
        if i not in x:
            x.append(i)
    return x
```
