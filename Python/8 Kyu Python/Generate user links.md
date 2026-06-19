# Generate user links

## Generate user links
Your task is to create userlinks for the url, you will be given a username and must return a valid link.

## Example
```
generate_link('matt c')
http://www.codewars.com/users/matt%20c
```

## reference
use this as a reference encoding

# Given Code

```{python}
def generate_link(user):
    pass
```

# My Solution

```{python}
import urllib.parse

def generate_link(user):
    baseurl = "http://www.codewars.com/users/"
    username = urllib.parse.quote(user)
    return f"{baseurl}{username}"
```
