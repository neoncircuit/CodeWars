# String matchup

Given two arrays of strings, return the number of times each string of the second array appears in the first array.

## Example

```
array1 = ['abc', 'abc', 'xyz', 'cde', 'uvw']
array2 = ['abc', 'cde', 'uap']
```

How many times do the elements in `array2` appear in `array1`?

- `'abc'` appears twice in the first array (2)
- `'cde'` appears only once (1)
- `'uap'` does not appear in the first array (0)

Therefore, `solve(array1, array2) = [2, 1, 0]`

Good luck!

# Given Code

```python
def solve(a,b):
    pass
```

# My Solution

```python
from typing import List
from collections import Counter

def solve(a: List[str], b: List[str]) -> List[int]:
    freq = Counter(a) 
    return [freq[x] for x in b]
```

# Complexity Analysis

**Time Complexity:** O(n)

**Space Complexity:** O(n)

**Explanation:**
**Time: O(n)** - Linear time complexity. The code iterates through the input once (using loops like for, while, forEach, map, filter, reduce). The number of operations grows proportionally with the input size.

**Space: O(n)** - Linear space complexity. Data structures (arrays, objects, sets, maps) were detected that may grow proportionally with input size.
