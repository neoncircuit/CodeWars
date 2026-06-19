# Adaptive Security System

A security system protects a network from intrusion attempts.

Hackers try to breach the system one by one, in the order given.

Each hacker has a skill level.

The system starts with a given security level.

Rules:

For each hacker:

- If the hacker's skill is strictly greater than the current security level, the hacker successfully breaches the system.
- Otherwise, the system blocks the attack and learns from it, increasing its security level.

Each blocked attack increases the security level by a fixed amount.

Your task is to return the number of successful breaches.

If the array is empty, return `0`.

Example
```
breachAttempts([7, 6, 8, 9], 6, 2)
```

Initial values
```
securityLevel = 6
increase = 2
```

Step-by-step
```
Hacker 7 vs security 6 → breach → security stays 6
Hacker 6 vs security 6 → blocked → security becomes 8
Hacker 8 vs security 8 → blocked → security becomes 10
Hacker 9 vs security 10 → blocked
```

Result
```
1
```

# Given Code

```python
def breach_attempts(hackers, security_level, increase):
    pass
```

# My Solution

```python
from typing import List

def breach_attempts(hackers: List[int], security_level: int, increase: int) -> int:
    if not hackers:
        return 0
    
    breaches = 0
    for attempt in hackers:
        if attempt > security_level:
            breaches += 1
        else:
            security_level += increase
    return breaches
```

# Complexity Analysis

**Time Complexity:** O(n)

**Space Complexity:** O(1)

**Explanation:**
**Time: O(n)** - Linear time complexity. The code iterates through the input once (using loops like for, while, forEach, map, filter, reduce). The number of operations grows proportionally with the input size.

**Space: O(1)** - Constant space complexity. The code uses a fixed amount of memory regardless of input size.
