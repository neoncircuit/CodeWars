# Minimum Perimeter of a Rectangle

A rectangle can be defined by two factors: `height` and `width`.

Its area is defined as the multiplication of the two: `height * width`.

Its perimeter is the sum of its four edges: `height + height + width + width`.

It is possible to create rectangles of the same area but different perimeters. For example, given an area of 45, the possible heights, widths and resultant perimeters would be:

```
(1, 45) = 92

(9, 5) = 28

(15, 3) = 36
```

Note that `(6, 7.5)` has an area of `45` too, but is discarded in this kata because its width is non integral.

The task is to write a function that, given an area as a positive integer, returns the smallest perimeter possible of a rectangle with integral side lengths.

Input range:
- `1 <= area <= 5 x 10 ^ 10`

# Given Code

```python
def minimum_perimeter(area):
    pass
```

# My Solution

```python
import math

def minimum_perimeter(area: int) -> int:
    if area < 1:
        raise ValueError("area must be >= 1")

    root = math.isqrt(area)
    perimeter_root = None
    perimeter_reg = None

    if math.pow(root, 2) == area:
        perimeter_root = 4 * root

    for height in range(root, 0, -1):
        if area % height == 0:
            width = area // height
            if height != width:
                perimeter_reg = 2 * (height + width)
                break  

    if perimeter_root is not None and perimeter_reg is not None:
        return min(perimeter_root, perimeter_reg)
    elif perimeter_root is not None:
        return perimeter_root
    elif perimeter_reg is not None:
        return perimeter_reg
    else: 
        return 4
```

# Complexity Analysis

**Time Complexity:** O(n)

**Space Complexity:** O(1)

**Explanation:**
**Time: O(n)** - Linear time complexity. The code iterates through the input once (using loops like for, while, forEach, map, filter, reduce). The number of operations grows proportionally with the input size.

**Space: O(1)** - Constant space complexity. The code uses a fixed amount of memory regardless of input size.
