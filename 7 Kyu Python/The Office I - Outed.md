# The Office I - Outed

Your colleagues have been looking over your shoulder. When you should have been doing your boring real job, you've been using the work computers to smash in endless hours of codewars.

In a team meeting, a terrible, awful person declares to the group that you aren't working. You're in trouble. You quickly have to gauge the feeling in the room to decide whether or not you should gather your things and leave.

Given an object ( `meet` ) containing team member names as keys, and their happiness rating out of 10 as the value, you need to assess the overall happiness rating of the group. If <= 5, return 'Get Out Now!'. Else return 'Nice Work Champ!'.

Happiness rating will be total score / number of people in the room.

Note that your boss is in the room ( `boss` ). Their score is worth double its face value (but they are still just one person!).

# Given Code

```python
def outed(meet, boss):
    pass # your code here!
```

# My Solution

```python
from typing import Set, Any

def outed(meet: Set[Any], boss: str) -> str:
    # your code here!
    total = sum(meet.values()) + meet[boss]
    res = total / len(meet)
    return "Nice Work Champ!" if res > 5 else "Get Out Now!"
```

# Complexity Analysis

**Time Complexity:** O(1)

**Space Complexity:** O(1)

**Explanation:**
**Time: O(1)** - Constant time complexity. The code performs a fixed number of operations regardless of input size. No loops or recursive calls that depend on input size were detected.

**Space: O(1)** - Constant space complexity. The code uses a fixed amount of memory regardless of input size.
