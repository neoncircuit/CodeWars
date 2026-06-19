# Functional Addition

Create a function `add(n)/Add(n)` which returns a function that always adds n to any number

Note for Java: the return type and methods have not been provided to make it a bit more challenging.

```
add_one = add(1)
add_one(3)  # 4

add_three = add(3)
add_three(3) # 6
```

# Given Code

```python
from typing import Callable

def add(n: int) -> Callable:
    pass
```

# My Solution

```python
from typing import Callable

def add(n: int) -> Callable:
    return lambda x: n + x
```

# Complexity Analysis

**Time Complexity:** O(1)

**Space Complexity:** O(1)

**Explanation:**
**Time: O(1)** - Constant time complexity. The code performs a fixed number of operations regardless of input size. No loops or recursive calls that depend on input size were detected.

**Space: O(1)** - Constant space complexity. The code uses a fixed amount of memory regardless of input size.
