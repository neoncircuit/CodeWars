# Word values

Given a string `"abc"` and assuming that each letter in the string has a value equal to its position in the alphabet, our string will have a value of `1 + 2 + 3 = 6`. This means that: `a = 1, b = 2, c = 3 ... z = 26`.

You will be given a list of strings and your task will be to return the values of the strings as explained above multiplied by the position of that string in the list. For our purpose, position begins with `1`.

`["abc", "abc abc"]` should return `[6, 24]` because of `[ 6 * 1, 12 * 2 ]`. Note how spaces are ignored.

`"abc"` has a value of `6`, while `"abc abc"` has a value of `12`. Now, the value at position `1` is multiplied by `1` while the value at position `2` is multiplied by `2`.

Input will only contain lowercase characters and spaces.

Good luck!

# Given Code

```python
def name_value(my_list):
  pass
```

# My Solution

```python
from typing import List

def name_value(my_list: List[str]) -> List[int]:
    res = []

    for position, name in enumerate(my_list, start=1):
        letter_sum = 0

        for char in name:
            if char == ' ':
                continue
            letter_sum += ord(char) - 96
        calculated_value = letter_sum * position
        res.append(calculated_value)

    return res
```

# Complexity Analysis

**Time Complexity:** O(n)

**Space Complexity:** O(n)

**Explanation:**
**Time: O(n)** - Linear time complexity. The code iterates through the input once (using loops like for, while, forEach, map, filter, reduce). The number of operations grows proportionally with the input size.

**Space: O(n)** - Linear space complexity. Data structures (arrays, objects, sets, maps) were detected that may grow proportionally with input size.
