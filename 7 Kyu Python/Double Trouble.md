# Double Trouble

Given an array of integers (x), and a target (t), you must find out if any two consecutive numbers in the array sum to t. If so, remove the second number.

## Example

```
x = [1, 2, 3, 4, 5]
t = 3

1+2 = t, so remove 2. No other pairs = t, so rest of array remains:

[1, 3, 4, 5]
```

Work through the array from left to right.

Return the resulting array.

# Given Code

```python
def trouble(x, t):
    pass
```

# My Solution

```python
def trouble(x: list[int], t: int) -> list[int]:
    idx = 0
    while idx < len(x) - 1:
        if x[idx] + x[idx+1] == t:
            x.pop(idx+1)
        else:
            idx += 1
    return x
```

# Complexity Analysis

**Time Complexity:** O(1)

**Space Complexity:** O(1)

**Explanation:**
**Time: O(1)** - Constant time complexity. The code performs a fixed number of operations regardless of input size. No loops or recursive calls that depend on input size were detected.

**Space: O(1)** - Constant space complexity. The code uses a fixed amount of memory regardless of input size.
