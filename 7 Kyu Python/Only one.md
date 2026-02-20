# Only one

Task: Write a function which returns `True` if ONLY ONE of the boolean flag is `True`, otherwise return `False`. If there are no boolean flag, return `False`

| Input	| Expected Output |
| :- | :- |
|No flags passed in |`False`|
|`True, False, False`|`True`|
|`True, False, False, True`|`False`|
|`False, False, False, False`|`False`|

# Given Code

```python
def only_one():
    pass
```

# My Solution

```python
def only_one(*bools: bool) -> bool:
    true_count = sum(1 for item in bools if item is True)
    return true_count == 1
```

# Complexity Analysis

**Time Complexity:** O(n)

**Space Complexity:** O(1)

**Explanation:**
**Time: O(n)** - Linear time complexity. The code iterates through the input once (using loops like for, while, forEach, map, filter, reduce). The number of operations grows proportionally with the input size.

**Space: O(1)** - Constant space complexity. The code uses a fixed amount of memory regardless of input size.
