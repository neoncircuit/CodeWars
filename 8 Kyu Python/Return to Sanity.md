# Return to Sanity

This function should return an object, but it's not doing what's intended. What's wrong?

# Given Code

```{python}
def mystery():
    results = {
    'sanity': 'Hello'}
    return
    results
```

# My Solution

```{python}
def mystery():
    results = {'sanity': 'Hello'}
    return results
```
