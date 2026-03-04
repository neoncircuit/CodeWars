# Number of Decimal Digits

Determine the total number of digits in the integer (`n>=0`) given as input to the function. For example, 9 is a single digit, 66 has 2 digits and 128685 has 6 digits. Be careful to avoid overflows/underflows.

# Given Code

```python
def digits(n):
    # your code here
    pass
```

# My Solution

```python
def digits(n: float) -> int:
    # your code here
    s = str(abs(n))
    return s.index('.') if '.' in s else len(s)
```

# Complexity Analysis

**Time Complexity:** O(1)

**Space Complexity:** O(1)

**Explanation:**
**Time: O(1)** - Constant time complexity. The code performs a fixed number of operations regardless of input size. No loops or recursive calls that depend on input size were detected.

**Space: O(1)** - Constant space complexity. The code uses a fixed amount of memory regardless of input size.
