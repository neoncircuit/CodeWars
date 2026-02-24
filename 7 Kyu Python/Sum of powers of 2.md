# Sum of powers of 2

Given a number `n`, you should find a set of numbers for which the sum equals `n`. This set must consist exclusively of values that are a power of `2` (eg: `2^0 => 1, 2^1 => 2, 2^2 => 4, ...`).

The function `powers` takes a single parameter, the number `n`, and should return an array of unique numbers.

## Criteria
The function will always receive a valid input: any positive integer between `1` and the max integer value for your language (eg: for JavaScript this would be `9007199254740991` otherwise known as `Number.MAX_SAFE_INTEGER`).

The function should return an array of numbers that are a power of 2 (`2^x = y`).

Each member of the returned array should be unique. (eg: the valid answer for `powers(2)` is `[2]`, not `[1, 1]`)

Members should be sorted in ascending order (small -> large). (eg: the valid answer for `powers(6)` is `[2, 4]`, not `[4, 2]`)

# Given Code

```python
# return an array of numbers (that are a power of 2)
# for which the input "n" is the sum
def powers(n):
    pass
```

# My Solution

```python
# return an array of numbers (that are a power of 2)
# for which the input "n" is the sum
from typing import List

def powers(n: int) -> List[int]:
    res = []
    i = 0
    while n:
        if n & 1:
            res.append(2**i)
        n >>= 1
        i += 1
    return res
```

# Complexity Analysis

**Time Complexity:** O(1)

**Space Complexity:** O(n)

**Explanation:**
**Time: O(1)** - Constant time complexity. The code performs a fixed number of operations regardless of input size. No loops or recursive calls that depend on input size were detected.

**Space: O(n)** - Linear space complexity. Data structures (arrays, objects, sets, maps) were detected that may grow proportionally with input size.
