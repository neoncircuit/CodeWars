# Get the Middle Character

You are going to be given a non-empty string. Your job is to return the middle character(s) of the string.

- If the string's length is odd, return the middle character.
- If the string's length is even, return the middle 2 characters.

## Examples

```
"test" --> "es"
"testing" --> "t"
"middle" --> "dd"
"A" --> "A"
```

# Given Code

```python
def get_middle(s):
    pass
```

# My Solution

```python
def get_middle(s: str) -> str:
    if len(s) == 1 or s == "":
        return s
    
    mid = len(s) // 2
    if len(s) % 2 == 0:
        return s[mid-1:mid+1]
    else:
        return s[mid]
```

# Complexity Analysis

**Time Complexity:** O(1)

**Space Complexity:** O(1)

**Explanation:**
**Time: O(1)** - Constant time complexity. The code performs a fixed number of operations regardless of input size. No loops or recursive calls that depend on input size were detected.

**Space: O(1)** - Constant space complexity. The code uses a fixed amount of memory regardless of input size.
