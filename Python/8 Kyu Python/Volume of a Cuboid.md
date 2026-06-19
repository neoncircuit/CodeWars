# Volume of a Cuboid

## Instructions

Bob needs a fast way to calculate the volume of a cuboid with three values: the `length`, `width` and `height` of the cuboid. Write a function to help Bob with this calculation.

## Given Code
```python
def get_volume_of_cuboid(length, width, height):
    # Code goes here...
    pass
```

## My Solution
```python
import math

def get_volume_of_cuboid(length, width, height):
    # Code goes here...
    volume = (length, width, height)
    return math.prod(volume)
```
