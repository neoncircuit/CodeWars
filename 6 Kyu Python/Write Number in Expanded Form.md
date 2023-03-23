# Write Number in Expanded Form

You will be given a number and you will need to return it as a string in Expanded Form. For example:
```
expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'
```
NOTE: All numbers will be whole numbers greater than 0.

If you liked this kata, check out part 2!!

# Given Code

```{python}
def expanded_form(num):
    pass
```

# My Solution

```{python}
def expanded_form(num):
    mult = 10
    res = []
    while num > 1:
        rem = num % mult
        if rem > 0:
            # Add as index 0 of res. Equivalent of res.unshift(rem) in JS
            res.insert(0, rem) 
        num -= rem
        mult *= 10
    # Convert each int in res to a string using the map and str function
    return " + ".join(map(str, res))
```

# My Solution 2

```{python}
def expanded_form(num):
    mult = 10
    res = []
    while num > 1:
        rem = num % mult
        if rem > 0:
            res.insert(0, rem) # Add as index 0 of res
        num -= rem
        mult *= 10
    return " + ".join(map(str, res))
```
