# Excel sheet column numbers

Write a function that, given a column title as it appears in an Excel sheet, returns its corresponding column number.

All column titles will be uppercase.

## Examples

```
Column title: "A" --> return 1
Column title: "Z" --> return 26
Column title: "AA" --> return 27
```

# Given Code

```python
def title_to_number(title):
    pass #your code here
```

# My Solution

```python
def title_to_number(title: str) -> int:
    res = 0
    for char in title:
        res = res * 26 + (ord(char) - ord('A') + 1)
    return res
```

# Complexity Analysis

**Time Complexity:** O(n)

**Space Complexity:** O(1)

**Explanation:**
**Time: O(n)** - Linear time complexity. The code iterates through the input once (using loops like for, while, forEach, map, filter, reduce). The number of operations grows proportionally with the input size.

**Space: O(1)** - Constant space complexity. The code uses a fixed amount of memory regardless of input size.
