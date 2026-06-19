# Fix string case

In this Kata, you will be given a string that may have mixed uppercase and lowercase letters and your task is to convert that string to either lowercase only or uppercase only based on:

- make as few changes as possible.
- if the string contains equal number of uppercase and lowercase letters, convert the string to lowercase.

For example:

```
solve("coDe") = "code". Lowercase characters > uppercase. Change only the "D" to lowercase.
solve("CODe") = "CODE". Uppercase characters > lowecase. Change only the "e" to uppercase.
solve("coDE") = "code". Upper == lowercase. Change all to lowercase.
```

More examples in test cases. Good luck!

# Given Code

```python
def solve(s):
    pass
```

# My Solution

```python
def solve(s: str) -> str:
    upper_count, lower_count = 0, 0
    for c in s:
        if c.isupper():
            upper_count += 1
        else:
            lower_count += 1
    
    return s.upper() if (upper_count > lower_count) else s.lower()
```

# Complexity Analysis

**Time Complexity:** O(n)

**Space Complexity:** O(1)

**Explanation:**
**Time: O(n)** - Linear time complexity. The code iterates through the input once (using loops like for, while, forEach, map, filter, reduce). The number of operations grows proportionally with the input size.

**Space: O(1)** - Constant space complexity. The code uses a fixed amount of memory regardless of input size.
