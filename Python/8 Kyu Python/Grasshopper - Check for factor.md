# Grasshopper - Check for factor

This function should test if the `factor` is a factor of base.

Return `true` if it is a factor or `false` if it is not.

## About factors
Factors are numbers you can multiply together to get another number.

2 and 3 are factors of 6 because: `2 * 3 = 6`

- You can find a factor by dividing numbers. If the remainder is 0 then the number is a factor.
- You can use the mod operator (`%`) in most languages to check for a remainder

For example 2 is not a factor of 7 because: `7 % 2 = 1`

Note: `base` is a non-negative number, `factor` is a positive number.

# Given Code

```python
def check_for_factor(base, factor):
    # your code here
```

# My Solution

```python
def check_for_factor(base: int, factor: int) -> bool:
    # your code here
    """
    Check if "factor" is a factor of "base"
    
    Args:
        - base: int - Base number
        - factor: int - Number that can be multiplied with other numbers
    Returns:
        Return True if "factor" is a factor of "base". Else False
    """
    return base % factor == 0
```

# Complexity Analysis

**Time Complexity:** O(1)

**Space Complexity:** O(1)

**Explanation:**
**Time: O(1)** - Constant time complexity. The code performs a fixed number of operations regardless of input size. No loops or recursive calls that depend on input size were detected.

**Space: O(1)** - Constant space complexity. The code uses a fixed amount of memory regardless of input size.
