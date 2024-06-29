# Is the date today

Write a simple function that takes as a parameter a date object and returns a boolean value representing whether the date is today or not.

Make sure that your function does not return a false positive by only checking the day.

# Given Code

```{python}
from datetime import datetime

def is_today(date): 
    # your code here
    pass
```

# My Solution

```{python}
from datetime import datetime

def is_today(date): 
    # your code here
    today = datetime.now().date()
    if date.date() == today:
        return True
    else: 
        return False
```
