# Keep Hydrated!

Nathan loves cycling.

Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.

You get given the time in hours and you need to return the number of litres Nathan will drink, rounded down.

For example:

```
time = 3 ----> litres = 1

time = 6.7---> litres = 3

time = 11.8--> litres = 5
```

# Given Code

```python
def litres(time):
    return 0
```

# My Solution

```python
import math

def litres(time: float) -> int:
    """
    Nathan drinks 0.5 litres of water per hour of cycling.
    
    Args:
        Number of hours as a float.
        
    Returns:
        Number of litres of water required, rounded down. 
    """
    return math.floor(time/2)
```

# Complexity Analysis

**Time Complexity:** O(log n)

**Space Complexity:** O(1)

**Explanation:**
**Time: O(log n)** - Logarithmic time complexity. The code appears to use a divide-and-conquer approach (like binary search), where the problem size is halved with each step. Very efficient for large inputs.

**Space: O(1)** - Constant space complexity. The code uses a fixed amount of memory regardless of input size.
