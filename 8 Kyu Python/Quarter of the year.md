# Quarter of the year

Given a month as an integer from 1 to 12, return to which quarter of the year it belongs as an integer number.

For example: month 2 (February), is part of the first quarter; month 6 (June), is part of the second quarter; and month 11 (November), is part of the fourth quarter.

Constraint:
- `1 <= month <= 12`

# Given Code

```python
def quarter_of(month):
    # your code here
    pass
```

# My Solution

```python
import math

def quarter_of(month: int) -> int:
    # your code here
    """
    Given a month as an integer from 1 to 12, 
    return to which quarter of the year it belongs as an integer number.
    
    Args:
        month: int - The month as an integer
    
    Returns:
        The quarter of the year as an integer. Eg. 3rd quarter returns 3
    """
    return math.ceil(month/3)
```

# Complexity Analysis

**Time Complexity:** O(1)

**Space Complexity:** O(1)

**Explanation:**
**Time: O(1)** - Constant time complexity. The code performs a fixed number of operations regardless of input size. No loops or recursive calls that depend on input size were detected.

**Space: O(1)** - Constant space complexity. The code uses a fixed amount of memory regardless of input size.
