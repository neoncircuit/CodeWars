# Be Concise IV - Index of an element in an array

Provided is a function which accepts two parameters in the following order: array, element and returns the index of the element if found and "Not found" otherwise. Your task is to shorten the code as much as possible in order to meet the character count requirements of the Kata.

**You may assume that all array elements are unique.**

The character limit is `60` (CoffeeScript), `85` (JavaScript, Python), `161` (Java).

# Given Code

```python
def find(array, element):
    for i in range(len(array)):
        if array[i] == element:
            return i;
    return 'Not found'
```

# My Solution

```python
def find(a, e):
    try: return a.index(e)
    except: return 'Not found'
```

# Complexity Analysis

**Time Complexity:** O(1)

**Space Complexity:** O(1)

**Explanation:**
**Time: O(1)** - Constant time complexity. The code performs a fixed number of operations regardless of input size. No loops or recursive calls that depend on input size were detected.

**Space: O(1)** - Constant space complexity. The code uses a fixed amount of memory regardless of input size.
