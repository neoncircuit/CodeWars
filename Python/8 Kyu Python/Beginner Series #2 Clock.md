# Beginner Series #2 Clock

Clock shows `h` hours, `m` minutes and `s` seconds after midnight.

Your task is to write a function which returns the time since midnight in milliseconds.

## Example:
```
h = 0
m = 1
s = 1

result = 61000
```

Input constraints:
- `0 <= h <= 23`
- `0 <= m <= 59`
- `0 <= s <= 59`

# Given Code

```python
def past(h, m, s):
    # Good Luck!
```

# My Solution

```python
def past(h: int, m: int, s: int) -> int:
    # Good Luck!
    """
    Return the time since midnight in milliseconds.
    
    
    Args:
        - h: int - Hour of the day
        - m: int - Minute of the day
        - s: int - Second of the day

    Returns:
        Time in milliseconds since midnight.
        Hour is 3.6e+6ms
        Minute is 60000ms
        Second is 1000ms
    """
    hour = (3.6e+6)*h
    min = 60000*m
    sec = 1000*s
    return hour + min + sec
```

# Complexity Analysis

**Time Complexity:** O(1)

**Space Complexity:** O(1)

**Explanation:**
**Time: O(1)** - Constant time complexity. The code performs a fixed number of operations regardless of input size. No loops or recursive calls that depend on input size were detected.

**Space: O(1)** - Constant space complexity. The code uses a fixed amount of memory regardless of input size.
