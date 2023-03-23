# Century From Year

Introduction
The first century spans from the year 1 up to and including the year 100, the second century - from the year 101 up to and including the year 200, etc.

Task
Given a year, return the century it is in.

Examples
```
1705 --> 18
1900 --> 19
1601 --> 17
2000 --> 20
```

Note: this kata uses strict construction as shown in the description and the examples, you can read more about it here

# Given Code

```{python}
def century(year):
    # Finish this :)
    return
```

# My Solution

```{python}
def century(year):
    # Finish this :)
    return (year + 99) // 100

"""
  ____                                                _               _       __              
 / _  |__ _  ___  _ __ __ _ _ __   ___ __ _  ___ __ _(_) __ _ _ __   (_)___  |_ \ _   _  __ _ 
| (_| |__` |/ _ \| '_ |__` | '_ \ / _ ' _` |/ _ ' _` | |/ _` | '_ \  | |__ \  _| | | | |/ _` |
 \__  |  | | (_) | |_) | | | |_) | | | | | | | | | | | | | | | |_) | | / __/ |_  | |_| | | | |
    |_|  |_|\___/| .__/  |_|_.__/|_| |_| |_|_| |_| |_|_|_| |_| .__/  |_\___|   |_|_.__/|_| |_|
                  \___|                                       \___|                           
"""
```


# My Solution 2

```{python}
import math

def century(year):
    # Finish this :)
    return math.ceil(year/100)

"""
  ____                                                _               _       __              
 / _  |__ _  ___  _ __ __ _ _ __   ___ __ _  ___ __ _(_) __ _ _ __   (_)___  |_ \ _   _  __ _ 
| (_| |__` |/ _ \| '_ |__` | '_ \ / _ ' _` |/ _ ' _` | |/ _` | '_ \  | |__ \  _| | | | |/ _` |
 \__  |  | | (_) | |_) | | | |_) | | | | | | | | | | | | | | | |_) | | / __/ |_  | |_| | | | |
    |_|  |_|\___/| .__/  |_|_.__/|_| |_| |_|_| |_| |_|_|_| |_| .__/  |_\___|   |_|_.__/|_| |_|
                  \___|                                       \___|                           
"""
```
