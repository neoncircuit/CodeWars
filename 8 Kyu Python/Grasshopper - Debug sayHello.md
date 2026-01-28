# Grasshopper - Debug sayHello

The starship Enterprise has run into some problem when creating a program to greet everyone as they come aboard. It is your job to fix the code and get the program working again!

Example output:
```
Hello, Mr. Spock
```

# Given Code

```python
def say_hello(name):
"Hello"
```

# My Solution

```python
def say_hello(name: str) -> str:
    """
    Fix code to greeting program.
    
    Args:
        - name: str - Name of the user

    Returns:
        Hello, {name}
    """
    return f"Hello, {name}"
```

# Complexity Analysis

**Time Complexity:** O(1)

**Space Complexity:** O(1)

**Explanation:**
**Time: O(1)** - Constant time complexity. The code performs a fixed number of operations regardless of input size. No loops or recursive calls that depend on input size were detected.

**Space: O(1)** - Constant space complexity. The code uses a fixed amount of memory regardless of input size.
