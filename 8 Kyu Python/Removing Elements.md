# Removing Elements

Take an array and remove every second element from the array. Always keep the first element and start removing with the next element.

## Example:
```
["Keep", "Remove", "Keep", "Remove", "Keep", ...] --> ["Keep", "Keep", "Keep", ...]
```

None of the arrays will be empty, so you don't have to worry about that!

# Given Code

```{python}
def remove_every_other(my_list):
    # Your code here!
    pass
```

# My Solution

```{python}
def remove_every_other(my_list):
    # Your code here!
    sorted = []
    for i in range(len(my_list)):
        if i % 2 == 0:
            sorted.append(my_list[i])
    return sorted
```

# My Solution 2

```{python}
def remove_every_other(my_list):
    # Your code here!
    return my_list[::2]
```
