# Thinkful - Logic Drills: Traffic light

You're writing code to control your town's traffic lights. You need a function to handle each change from `green`, to `yellow`, to `red`, and then to `green` again.

Complete the function that takes a string as an argument representing the current state of the light and returns a string representing the state the light should change to.

For example, when the input is `green`, output should be `yellow`.

# Given Code

```python
def update_light(current):
    # Your code here.
```

# My Solution

```python
def update_light(current: str) -> str:
    # Your code here.
    return "yellow" if current == "green" else "red" if current == "yellow" else "green"
```

# Complexity Analysis

**Time Complexity:** O(1)

**Space Complexity:** O(1)

**Explanation:**
**Time: O(1)** - Constant time complexity. The code performs a fixed number of operations regardless of input size. No loops or recursive calls that depend on input size were detected.

**Space: O(1)** - Constant space complexity. The code uses a fixed amount of memory regardless of input size.
