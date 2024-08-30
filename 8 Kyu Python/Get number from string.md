# Get number from string

Write a function which removes from string all non-digit characters and parse the remaining to number. E.g: "hell5o wor6ld" -> 56

Function:
```
getNumberFromString(s)
```

# Given Code

```{python}
def get_number_from_string(st):
    pass
```

# My Solution

```{python}
def get_number_from_string(st):
    numbers = ""
    for i in st:
        if i.isdigit():
            numbers += i          
    return int(numbers)
```
