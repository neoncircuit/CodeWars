# Area of a Square

## Instructions

Complete the function that calculates the area of the red square, when the length of the circular arc `A` is given as the input. Return the result rounded to two decimals.

![alt text](http://i.imgur.com/nJrae8n.png)

Note: use the π value provided in your language (`Math::PI`, `M_PI`, `math.pi`, etc)




## Given Code
```python
def square_area(A):
    # your code here
```

## My Solution
```python
import math

def square_area(A:int):
    # your code here
    r = (2 * A) / math.pi 
    area = math.pow(r, 2)
    return round(area, 2)
```
