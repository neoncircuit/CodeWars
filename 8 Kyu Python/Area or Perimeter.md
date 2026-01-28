# Area or Perimeter

You are given the `length` and `width` of a 4-sided polygon. The polygon can either be a rectangle or a square.
If it is a square, return its area. If it is a rectangle, return its perimeter.

## Example(Input1, Input2 --> Output):

```
6, 10 --> 32
3, 3 --> 9
```

**Note**: for the purposes of this kata you will assume that it is a square if its length and width are equal, otherwise it is a rectangle.

# Given Code

```python
def area_or_perimeter(l , w):
    # return your answer
```

# My Solution

```python
def area_or_perimeter(l: int , w: int) -> int:
    # return your answer
    """
    Given a 4 sided polygon, return area if it is a square, otherwise perimeter if rectangle
    
    Args:
        l: int - Length of the polygon
        w: int - Width of the polygon
        
    Returns:
        Area of the polygon if it is a square.
        Perimeter of the polygon if it is a rectangle
    """
    return l*w if (l == w) else (l+w)*2
```

# Complexity Analysis

**Time Complexity:** O(1)

**Space Complexity:** O(1)

**Explanation:**
**Time: O(1)** - Constant time complexity. The code performs a fixed number of operations regardless of input size. No loops or recursive calls that depend on input size were detected.

**Space: O(1)** - Constant space complexity. The code uses a fixed amount of memory regardless of input size.
