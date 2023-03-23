# Sum of the first nth term of Series

## Task:
Your task is to write a function which returns the sum of following series upto nth term(parameter).
```
Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...
```

## Rules:
You need to round the answer to 2 decimal places and return it as String.

If the given value is 0 then it should return 0.00

You will only be given Natural Numbers as arguments.

## Examples:(Input --> Output)
```
1 --> 1 --> "1.00"
2 --> 1 + 1/4 --> "1.25"
5 --> 1 + 1/4 + 1/7 + 1/10 + 1/13 --> "1.57"
```

# Given Code

```{python}
def series_sum(n):
    # Happy Coding ^_^
```

# My Solution

```{python}
def series_sum(n):
    # Happy Coding ^_^
    output = 0.0
    for i in range(n):
        output += 1 / (1 + i*3)
    return '%.2f' % output
```

# My Solution 2

```{python}
def series_sum(n):
    # Happy Coding ^_^
    fractions = []
    for n in range(1, 3*n - 1, 3):
        fractions.append(1/n)
    return "{:.2f}".format(sum(fractions))
```
