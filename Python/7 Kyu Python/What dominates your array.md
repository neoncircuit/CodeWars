# What dominates your array?

A zero-indexed array `arr` consisting of n integers is given. The dominator of array `arr` is the value that occurs in more than half of the elements of `arr`.
For example, consider array `arr` such that `arr = [3,4,3,2,3,1,3,3]`
The dominator of `arr` is 3 because it occurs in 5 out of 8 elements of `arr` and 5 is more than a half of 8.
Write a function `dominator(arr)` that, given a zero-indexed array `arr` consisting of n integers, returns the dominator of `arr`. The function should return −1 if array does not have a dominator. All values in `arr` will be >=0.

# Given Code

```python
def dominator(arr):
    #your code here
```

# My Solution

```python
from collections import Counter

def dominator(arr: list[int]) -> int:
    if not arr:
        return -1
    
    counts = Counter(arr)
    candidate, appearance = counts.most_common(1)[0]
    
    if appearance > len(arr) // 2:
        return candidate
    else: 
        return -1
```

# Complexity Analysis

**Time Complexity:** O(1)

**Space Complexity:** O(1)

**Explanation:**
**Time: O(1)** - Constant time complexity. The code performs a fixed number of operations regardless of input size. No loops or recursive calls that depend on input size were detected.

**Space: O(1)** - Constant space complexity. The code uses a fixed amount of memory regardless of input size.
