# Regex validate PIN code

ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but ```exactly``` 4 digits or exactly 6 digits.

If the function is passed a valid PIN string, return ```true```, else return ```false```.

## Examples (Input --> Output)
```
"1234"   -->  true
"12345"  -->  false
"a234"   -->  false
```

# Given Code

```{python}
def validate_pin(pin):
    #return true or false
```

# My Solution

```{python}
def validate_pin(pin):
    #return true or false
    return (len(pin) == 4 or len(pin) == 6) and pin.isnumeric()
```
