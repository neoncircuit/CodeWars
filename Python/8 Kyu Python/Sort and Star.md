# Sort and Star

You will be given a list of strings. You must sort it alphabetically (case-sensitive, and based on the ASCII values of the chars) and then return the first value.

The returned value must be a string, and have "***" between each of its letters.

You should not remove or add elements from/to the array.

# Given Code

```{python}
def two_sort(array):
    # your code here
```

# My Solution

```{python}
def two_sort(array):
    array.sort() # Alphabetical sort
    
    x = array[0] # First string from sorted array
    
    y = '***'.join(x) # Use '***' to seperate each character in First String
    
    return y
```
