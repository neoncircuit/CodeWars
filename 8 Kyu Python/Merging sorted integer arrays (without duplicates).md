# Merging sorted integer arrays (without duplicates)

Write a function that merges two sorted arrays into a single one. The arrays only contain integers. Also, the final outcome must be sorted and not have any duplicate.

# Given Code

```{python}
def merge_arrays(first, second): 
    # your code here
    pass
```

# My Solution

```{python}
def merge_arrays(first, second): 
    # your code here
    return sorted(set(first + second))
```
