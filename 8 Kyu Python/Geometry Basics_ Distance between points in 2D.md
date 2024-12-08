# Geometry Basics: Distance between points in 2D

## Instructions

This series of katas will introduce you to basics of doing geometry with computers.

`Point` objects have attributes `x` and `y`.

Write a function calculating distance between `Point a` and `Point b`.

Input coordinates fit in range `-50 ≤ x, y ≤ 50`. Tests compare expected result and actual answer with tolerance of `1e-6`.


## Given Code
```python
def distance_between_points(a, b):
    return 0 # your code here
```

## My Solution
```python
import math

def distance_between_points(a, b):
    # your code here
    x1, y1 = a.x, a.y
    x2, y2 = b.x, b.y
    x = math.pow(x2-x1, 2)
    y = math.pow(y2-y1, 2)
    return math.sqrt(x+y)
```
