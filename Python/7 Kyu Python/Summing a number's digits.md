# Summing a number's digits

Write a function which takes a number as input and returns the sum of the absolute value of each of the number's decimal digits.

For example: (Input --> Output)

```
10 --> 1
99 --> 18
-32 --> 5
```

Let's assume that all numbers in the input will be integer values.

# Given Code

```{python}
def sum_digits(number):
    pass
```

# My Solution

```{python}
def sum_digits(number: int) -> int:
    abs_number: int = abs(number)
    str_number: str = str(abs_number)
    digit_sum: int = 0
    
    for digit in str_number:
        digit_sum += int(digit)
        
    return digit_sum
```
