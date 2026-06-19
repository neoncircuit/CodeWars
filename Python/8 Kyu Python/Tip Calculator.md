# Tip Calculator

Complete the function, which calculates how much you need to tip based on the total amount of the bill and the service.

You need to consider the following ratings:

- Terrible: tip 0%
- Poor: tip 5%
- Good: tip 10%
- Great: tip 15%
- Excellent: tip 20%

The rating is case insensitive (so "great" = "GREAT"). If an unrecognised rating is received, then you need to return:

- "Rating not recognised" in Javascript, Python and Ruby...
- ...or null in Java
- ...or -1 in C#

Because you're a nice person, you always round up the tip, regardless of the service.

# Given Code

```{python}
def calculate_tip(amount, rating):
    #your code here
```

# My Solution

```{python}
from math import ceil

def calculate_tip(amount, rating):
    rating = rating.lower()
    
    #your code here
    match rating:
        case "terrible":
            return 0
        case "poor":
            return ceil(5/100 * amount)
        case "good":
            return ceil(10/100 * amount)
        case "great":
            return ceil(15/100 * amount)
        case "excellent":
            return ceil(20/100 * amount)
        case _:
            return "Rating not recognised"
```
