# Simple multiplication

This kata is about multiplying a given number by eight if it is an even number and by nine otherwise.

# Given Code

```python
def simple_multiplication(number) :
    # Your code goes here
```

# My Solution

```python
def simple_multiplication(number: int) -> int:
    # Your code goes here
    """
    Multiply a number by 8 if even. Else multiply by 9
    
    Args:
        number: int - Input number
        
    Returns:
        number*8 if even 
        number*9 if odd
    """
    return number*8 if (number%2 == 0) else number*9
```

# Complexity Analysis

**Time Complexity:** O(1)

**Space Complexity:** O(1)

**Explanation:**
**Time: O(1)** - Constant time complexity. The code performs a fixed number of operations regardless of input size. No loops or recursive calls that depend on input size were detected.

**Space: O(1)** - Constant space complexity. The code uses a fixed amount of memory regardless of input size.
