# Are You Playing Banjo?

Create a function which answers the question "Are you playing banjo?".
If your name starts with the letter "R" or lower case "r", you are playing banjo!

The function takes a name as its only argument, and returns one of the following strings:

```
name + " plays banjo" 
name + " does not play banjo"
```

Names given are always valid strings.

# Given Code

```python
def are_you_playing_banjo(name):
    # Implement me!
    return name
```

# My Solution

```python
def are_you_playing_banjo(name: str) -> str:
    # Implement me!
    plays_banjo: str = f"{name} plays banjo"
    plays_banjo_not: str = f"{name} does not play banjo"
    return plays_banjo if (name.lower().startswith("r")) else plays_banjo_not
```

# Complexity Analysis

**Time Complexity:** O(1)

**Space Complexity:** O(1)

**Explanation:**
**Time: O(1)** - Constant time complexity. The code performs a fixed number of operations regardless of input size. No loops or recursive calls that depend on input size were detected.

**Space: O(1)** - Constant space complexity. The code uses a fixed amount of memory regardless of input size.
