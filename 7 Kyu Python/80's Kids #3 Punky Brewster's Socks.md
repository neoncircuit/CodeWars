# 80's Kids #3: Punky Brewster's Socks

Punky loves wearing different colored socks, but Henry can't stand it.

Given an array of different colored socks, return a pair depending on who was picking them out.

Example:

```
get_socks('Punky', ['red','blue','blue','green']) -> ['red', 'blue']
```

Note that Punky can have any two colored socks, in any order, as long as they are different and both exist. Henry always picks a matching pair.

If there is no possible combination of socks, return an empty array.

# Given Code

```python
def get_socks(name, socks):
    #your code here
    pass
```

# My Solution

```python
from typing import List
from collections import Counter

def get_socks(name: str, socks: List[str]) -> List[str]:
    #your code here
    counts = Counter(socks)
    
    if name == "Henry":
        for color, count in counts.items():
            if count >= 2:
                return [color, color]
        return []
    else:
        unique_colors = list(counts.keys())
        return unique_colors[:2] if (len(unique_colors) >= 2) else []
```

# Complexity Analysis

**Time Complexity:** O(1)

**Space Complexity:** O(n)

**Explanation:**
**Time: O(1)** - Constant time complexity. The code performs a fixed number of operations regardless of input size. No loops or recursive calls that depend on input size were detected.

**Space: O(n)** - Linear space complexity. Data structures (arrays, objects, sets, maps) were detected that may grow proportionally with input size.
