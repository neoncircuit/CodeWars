# Return Two Highest Values in List

In this kata, your job is to return the two distinct highest values in a list. If there're less than 2 unique values, return as many of them, as possible.

The result should also be ordered from highest to lowest.

## Examples

[4, 10, 10, 9]  =>  [10, 9]
[1, 1, 1]  =>  [1]
[]  =>  []

# Given Code

```{python}
def two_highest(arg1):
    pass
```

# My Solution

```{python}
# Create a set of distinct values from the input list arg1
    distinct_values = set(arg1)

    # Sort the distinct values in descending order
    sorted_values = sorted(distinct_values, reverse=True)

    # Check if there are at least two distinct values
    if len(sorted_values) >= 2:
        # Return the first two values if there are at least two
        return sorted_values[:2]
    elif len(sorted_values) == 1:
        # If there is only one distinct value, return it
        return [sorted_values[0]]
    else:
        # If there are no distinct values, return an empty list
        return []
```
