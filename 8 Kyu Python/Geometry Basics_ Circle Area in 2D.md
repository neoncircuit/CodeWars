# Geometry Basics: Circle Area in 2D

## Instructions

This series of katas will introduce you to basics of doing geometry with computers.

Write the function `circleArea`/`CircleArea` which takes in a `Circle` object and calculates the area of that circle.

The `Circle` class can be seen below:

```
class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
```

And the `Point` class can be seen below:

```
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

## Given Code
```python
def circle_area(circle):
    # your solution here
```

## My Solution
```python
import math

def circle_area(circle):
    # your solution here
    return math.pi * math.pow((circle.radius), 2)
```
