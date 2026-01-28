# Third Angle of a Triangle

You are given two interior angles (in degrees) of a triangle.

Write a function to return the 3rd.

Note: only positive integers will be tested.

[Triangle](https://en.wikipedia.org/wiki/Triangle)

# Given Code

```python
def other_angle(a, b):
    pass
```

# My Solution

```python
def other_angle(a: int, b: int) -> int:
    """
    Given 2 interior angles of a triangle, return the 3rd.
    
    Args:
        - a: int - Angle a of the triangle
        - b: int - Angle b of the triangle
        
    Returns:
        180 - a - b because all 3 angles of a triangle add up to 180 degrees.
    """
    return 180 - a - b
```

# Complexity Analysis

**Time Complexity:** O(1)

**Space Complexity:** O(1)

**Explanation:**
**Time: O(1)** - Constant time complexity. The code performs a fixed number of operations regardless of input size. No loops or recursive calls that depend on input size were detected.

**Space: O(1)** - Constant space complexity. The code uses a fixed amount of memory regardless of input size.
