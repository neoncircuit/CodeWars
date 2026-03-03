# Multiples By Permutations II

We have two consecutive integers `k1` and `k2`, where `k2 = k1 + 1`

We need to calculate the lowest strictly positive integer `n`, such that the values `n ⋅ k1` and `n ⋅ k2` have the same digits but in different order.

E.g. #1:

```
k1 = 100
k2 = 101
n = 8919
#Because 8919 * 100 = 891900 
and      8919 * 101 = 900819
```

E.g. # 2:

```
k1 = 325
k2 = 326
n = 477
#Because 477 * 325 = 155025
and      477 * 326 = 155502
```

Your task is to prepare a function that will receive the value of `k` and outputs the value of `n`.

The examples given above will be:

```
Input: 100 --> Return: 8919
Input: 325 --> Return:  477
```

Features of the random tests

```
10 < k < 10.000.000.000.000.000 (For Python, Ruby and Haskell)
10 < k < 1.000.000.000  (For Javascript and D 1e9)
```

Enjoy it!!

# Given Code

```python
def find_lowest_int(k):
    pass
```

# My Solution

```python
from typing import Optional
from collections import Counter

def digit_signature(num: int) -> Counter[str]:
    return Counter(str(num))

def find_lowest_int(k: int, max_search: int = 1000000) -> Optional[int]:
    for n in range(1, max_search, 1):
        a = k * n
        b = (k + 1) * n
        if digit_signature(a) == digit_signature(b):
            return n
    return None
```

# Complexity Analysis

**Time Complexity:** O(n)

**Space Complexity:** O(n)

**Explanation:**
**Time: O(n)** - Linear time complexity. The code iterates through the input once (using loops like for, while, forEach, map, filter, reduce). The number of operations grows proportionally with the input size.

**Space: O(n)** - Linear space complexity. Recursion was detected, which uses call stack space proportional to the recursion depth.
