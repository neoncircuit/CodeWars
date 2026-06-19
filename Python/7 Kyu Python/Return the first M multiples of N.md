# Return the first M multiples of N

Implement a function that takes two numbers `m` and `n` and returns an array of the first `m` multiples of the real number `n`. Assume that `m` is a positive integer.

Ex.
```
(3, 5.0) --> [5.0, 10.0, 15.0]
```

# Given Code

```python
def multiples(m: int, n: int | float) -> list[int] | list[float]:
    # Implement me! :)
    return []
```

# My Solution

```python
def multiples(m: int, n: int | float) -> list[int] | list[float]:
    # Implement me! :)
    res = []
    idx = 1
    for i in range(0, m, 1):
        res.append(idx*n)
        idx += 1
    return res
```

# Complexity Analysis

**Time Complexity:** O(n)

**Space Complexity:** O(n)

**Explanation:**
**Time: O(n)** - Linear time complexity. The code iterates through the input once (using loops like for, while, forEach, map, filter, reduce). The number of operations grows proportionally with the input size.

**Space: O(n)** - Linear space complexity. Data structures (arrays, objects, sets, maps) were detected that may grow proportionally with input size.
