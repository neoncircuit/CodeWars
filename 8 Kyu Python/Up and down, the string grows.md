# Up and down, the string grows

Many programming languages provide the functionality of converting a string to uppercase or lowercase. For example, `upcase`/`downcase` in Ruby, `upper`/`lower` in Python, and `toUpperCase`/`toLowerCase` in Java/JavaScript, `uppercase`/`lowercase` in Kotlin. Typically, these methods won't change the size of the string.

For example, in Ruby, `str.upcase.downcase.size == str.size` is `true` for most cases.

However, in some special cases, the length of the transformed string may be longer than the original. Can you find a string that satisfies this criteria?

For example, in Ruby, That means `str.upcase.downcase.size > str.size`

You should just set the value of `STRANGE_STRING` to meet the previous criteria.

Note: Meta programming is not allowed in this kata. So, the size of your solution is limited.

# Given Code

```python
STRANGE_STRING = 'foo'
```

# My Solution

```python
STRANGE_STRING='ß'
```

# Complexity Analysis

**Time Complexity:** O(1)

**Space Complexity:** O(1)

**Explanation:**
**Time: O(1)** - Constant time complexity. The code performs a fixed number of operations regardless of input size. No loops or recursive calls that depend on input size were detected.

**Space: O(1)** - Constant space complexity. The code uses a fixed amount of memory regardless of input size.
