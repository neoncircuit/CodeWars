# String repeat

Write a function that accepts a non-negative integer n and a string s as parameters, and returns a string of s repeated exactly n times.

## Examples (input -> output)
```
6, "I"     -> "IIIIII"
5, "Hello" -> "HelloHelloHelloHelloHello"
```

# Given Code

```python
def repeat_str(repeat, string):
    return ''
```

# My Solution

```python
def repeat_str(repeat: int, string: str) -> str:
    """
    Given a non-negative integer n and a string s as parameters,
    return a string of s exactly n times.
    
    Args:
        - repeat: int - The number of times you want to duplicate the string
        - string: str - The string you want to duplicate
        
    Returns:
        - The duplicated string.
    """
    return "".join(string*repeat)
```

# Complexity Analysis

**Time Complexity:** O(1)

**Space Complexity:** O(1)

**Explanation:**
**Time: O(1)** - Constant time complexity. The code performs a fixed number of operations regardless of input size. No loops or recursive calls that depend on input size were detected.

**Space: O(1)** - Constant space complexity. The code uses a fixed amount of memory regardless of input size.
