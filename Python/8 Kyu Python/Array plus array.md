# Array plus array

I'm new to coding and now I want to get the sum of two arrays... Actually the sum of all their elements. I'll appreciate for your help.

P.S. Each array includes only integer numbers. Output is a number too.

# Given Code

```{python}
def array_plus_array(arr1,arr2):
    pass
```

# My Solution

```{python}
from itertools import chain

def array_plus_array(arr1,arr2):
    return sum(chain(arr1, arr2))
```
