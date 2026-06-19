# Playing with cubes II

Hey Codewarrior!

In the [previous kata](https://www.codewars.com/kata/55c0a79e20be94c91400014b), you have implemented a **Cube** class, but now we need your help again! I'm talking about constructors. We don't have one. Let's code one (or more) such that one can instantiate an object via it, handling either no arguments or a single integer.

Also we got a problem with negative values. Correct the code so negative values will be switched to positive ones!

The constructor taking no arguments should assign 0 to Cube's Side property.

# Given Code

```python
class Cube(object):
    # This cube needs help
    # Define a constructor which takes one integer, or handles no args
    
    def get_side(self):
        """Return the side of the Cube"""
        return self.__side

    def set_side(self, new_side):
        """Set the value of the Cube's side."""
        self.__side = new_side
```

# My Solution

```python
class Cube(object):
    # This cube needs help
    # Define a constructor which takes one integer, or handles no args
    def __init__(self, side: int = 0) -> int:
        self.set_side(side)
    
    def get_side(self) -> int:
        """Return the side of the Cube"""
        return self.__side

    def set_side(self, new_side: int) -> int:
        """Set the value of the Cube's side."""
        self.__side = abs(new_side)
```

# Complexity Analysis

**Time Complexity:** O(1)

**Space Complexity:** O(n)

**Explanation:**
**Time: O(1)** - Constant time complexity. The code performs a fixed number of operations regardless of input size. No loops or recursive calls that depend on input size were detected.

**Space: O(n)** - Linear space complexity. Recursion was detected, which uses call stack space proportional to the recursion depth.
