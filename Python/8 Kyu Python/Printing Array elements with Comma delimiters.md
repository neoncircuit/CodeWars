# Printing Array elements with Comma delimiters

Input: Array of elements

["h","o","l","a"]

Output: String with comma delimited elements of the array in th same order.

"h,o,l,a"

Note: if this seems too simple for you try the next level

# Given Code

```{python}
def print_array(arr):
    #your code here
```

# My Solution

```{python}
def print_array(arr):
    if not arr:
        return ""
    # Convert each element to a string and then join them
    return ','.join(map(str, arr))
```
