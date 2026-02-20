# Make Equal

Given an array of integers `a` and integers `t` and `x`, count how many elements in the array you can make equal to `t` by increasing / decreasing it by `x` (or doing nothing). EASY!

```
# ex 1

a = [11, 5, 3]
t = 7
x = 2

count(a, t, x) # => 3
```

- you can make 11 equal to 7 by subtracting 2 twice
- you can make 5 equal to 7 by adding 2
- you can make 3 equal to 7 by adding 2 twice

```
# ex 2

a = [-4,6,8]
t = -7
x = -3

count(a, t, x) # => 2
```

## Constraints
- `-1018 <= a[i],t,x <= 1018`
- `3 <= |a| <= 104`

# Given Code

```python
def count(a, t, x):
    pass
```

# My Solution

```python
def count(a: list[int], t: int, x: int) -> int:
    if x == 0:
        return sum(1 for num in a if num == t)
    
    res = 0
    for num in a:
        if abs(t - num) % x == 0:
            res += 1
    return res
```

# Complexity Analysis

**Time Complexity:** O(n)

**Space Complexity:** O(1)

**Explanation:**
**Time: O(n)** - Linear time complexity. The code iterates through the input once (using loops like for, while, forEach, map, filter, reduce). The number of operations grows proportionally with the input size.

**Space: O(1)** - Constant space complexity. The code uses a fixed amount of memory regardless of input size.
