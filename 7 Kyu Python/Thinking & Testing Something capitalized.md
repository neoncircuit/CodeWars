# Thinking & Testing : Something capitalized

No Story

No Description

Only by Thinking and Testing

Look at the results of the testcases, and guess the code!

# Given Code

```python
def testit(s):
    pass # Your code here
```

# My Solution

```python
def testit(s: str) -> str:
    # Your code here
    words = s.split(" ")
    res = []
    
    for word in words:
        if len(word) == 0:
            res.append("")
        elif len(word) == 1:
            res.append(word.upper())
        else:
            res.append(word[:-1] + word[-1].upper())
            
    return " ".join(res)
```

# Complexity Analysis

**Time Complexity:** O(n)

**Space Complexity:** O(n)

**Explanation:**
**Time: O(n)** - Linear time complexity. The code iterates through the input once (using loops like for, while, forEach, map, filter, reduce). The number of operations grows proportionally with the input size.

**Space: O(n)** - Linear space complexity. Data structures (arrays, objects, sets, maps) were detected that may grow proportionally with input size.
