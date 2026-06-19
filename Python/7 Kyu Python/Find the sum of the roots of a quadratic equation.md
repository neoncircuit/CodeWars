# Find the sum of the roots of a quadratic equation

## Instructions

Implement function which will return sum of roots of a quadratic equation rounded to 2 decimal places, if there are any possible roots. Otherwise return **None/null/nil/nothing**. If you use discriminant,when discriminant = 0, x1 = x2 = root => return sum of both roots. There will always be valid arguments.

Quadratic equation - [Quadratic Equation](https://en.wikipedia.org/wiki/Quadratic_equation)



## Given Code
```python
def roots(a,b,c):
    return None
```

## My Solution
```python
import math

def roots(a:int, b:int, c:int):
    discriminant = math.pow(b, 2) - 4*a*c
    
    # return None if discriminant is negative, 
    # otherwise sum of roots is always -b/a regardless of discriminant
    return None if discriminant < 0 else round(-b/a, 2) 
```
