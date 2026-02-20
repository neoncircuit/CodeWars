# Perimeter sequence

The first three stages of a sequence are shown.

![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAXMAAABhAQMAAAAeHdP1AAAABlBMVEX///8AAABVwtN+AAAAm0lEQVRYw+3YMQrCQBAF0Fls7OIBAnuNdF5tjrZHsrQQvoMOKF/UhBCSwP+wLPx5bDnFmrL5dAB8gq/h24K+Nyvy8vLyG/QFwIV9dNcv/sCzikduY30f55d3s4G9xyUvLy+/M18BsD9H5+Rrdjl7eTzTaN9m9+nzrUbvd9kNQdifzAr7Y3Ty8vLyq/nZ+/C/5/1ccubv/wnUjc4d8QgoHd+N+FEAAAAASUVORK5CYII=)

The blocksize is `a` by `a` and `a ≥ 1`.

What is the perimeter of the `n`th shape in the sequence (`n ≥ 1`) ?

# Given Code

```python
def perimeter_sequence(a, n): 
    # your code here
    pass
```

# My Solution

```python
def perimeter_sequence(a: int, n: int) -> int: 
    # your code here
    return a * n * 4
```

# Complexity Analysis

**Time Complexity:** O(1)

**Space Complexity:** O(1)

**Explanation:**
**Time: O(1)** - Constant time complexity. The code performs a fixed number of operations regardless of input size. No loops or recursive calls that depend on input size were detected.

**Space: O(1)** - Constant space complexity. The code uses a fixed amount of memory regardless of input size.
