# Find the Slope

Given an array of 4 integers
`[a,b,c,d]` representing two points `(a, b)` and `(c, d)`, return a string representation of the slope of the line joining these two points.

For an undefined slope (division by 0), return `undefined`. Note that the "undefined" is case-sensitive.

```
a:x1
b:y1
c:x2
d:y2
```

Assume that `[a,b,c,d]` and the answer are all integers (no floating numbers!). Slope: [Wikipedia - Slope](https://en.wikipedia.org/wiki/Slope)

# Given Code

```python
def find_slope(points):
    return "undefined"
```

# My Solution

```python
import math

def find_slope(points: list[int]) -> str:
    a, b, c, d = points
    try: 
        m: int = math.floor((d - b)/(c - a))
        return str(m)
    except ZeroDivisionError:
        return "undefined"
```

# Complexity Analysis

**Time Complexity:** O(1)

**Space Complexity:** O(1)

**Explanation:**
**Time: O(1)** - Constant time complexity. The code performs a fixed number of operations regardless of input size. No loops or recursive calls that depend on input size were detected.

**Space: O(1)** - Constant space complexity. The code uses a fixed amount of memory regardless of input size.
