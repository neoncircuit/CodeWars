# Sequence to 1

## Task
Given the number n, return the sequence of numbers from `n` to `1`.

## Range
The number n can be negative and also large number: `-9999  <=  n  <=  9999`

## Examples
```
n =  5    >>     5, 4, 3, 2, 1
n = -1    >>    -1, 0, 1
```

# Given Code

```python
def seq_to_one(n):
    pass
```

# My Solution

```python
def seq_to_one(n: int) -> list[int]:
    int_min, int_max = -9999, 9999
    while n >= int_min and n <= int_max:
        return list(range(n, 0, -1)) if n >= 1 else list(range(n, 2, 1))
```

# Complexity Analysis

**Time Complexity:** O(1)

**Space Complexity:** O(n)

**Explanation:**
**Time: O(1)** - Constant time complexity. The code performs a fixed number of operations regardless of input size. No loops or recursive calls that depend on input size were detected.

**Space: O(n)** - Linear space complexity. Data structures (arrays, objects, sets, maps) were detected that may grow proportionally with input size.
