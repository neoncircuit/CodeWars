# Convert boolean values to strings 'Yes' or 'No'.

Complete the method that takes a boolean value and return a `"Yes"` string for `true`, or a `"No"` string for `false`.

# Given Code

```python
def bool_to_word(boolean):
    # TODO
```

# My Solution

```python
def bool_to_word(boolean: bool) -> str:
    # TODO
    """
    Convert boolean value to "Yes" or "No"
    
    Args:
        - boolean: bool - Either True of False
        
    Returns:
        - "Yes" if boolean = True
        - "No" if boolean = False
    """
    return "Yes" if boolean else "No"
```

# Complexity Analysis

**Time Complexity:** O(1)

**Space Complexity:** O(1)

**Explanation:**
**Time: O(1)** - Constant time complexity. The code performs a fixed number of operations regardless of input size. No loops or recursive calls that depend on input size were detected.

**Space: O(1)** - Constant space complexity. The code uses a fixed amount of memory regardless of input size.
