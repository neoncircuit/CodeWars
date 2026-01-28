# Find Maximum and Minimum Values of a List

Your task is to make two functions ( `max` and `min`, or `maximum` and `minimum`, etc., depending on the language ) that receive a list of integers as input, and return the largest and lowest number in that list, respectively. Each function returns one number.

## Examples (Input -> Output)
```
* [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
* [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
* [42, 54, 65, 87, 0]             -> min = 0, max = 87
* [5]                             -> min = 5, max = 5
```

## Notes
You may consider that there will not be any empty arrays/vectors.

# Given Code

```python
def minimum(arr):
    #your code here...

def maximum(arr):
    #...and here
```

# My Solution

```python
def minimum(arr: list[int]) -> int:
    #your code here...
    arr.sort()
    return arr[0]

def maximum(arr: list[int]) -> int:
    #...and here
    arr.sort()
    return arr[-1]
```

# Complexity Analysis

**Time Complexity:** O(n log n)

**Space Complexity:** O(1)

**Explanation:**
**Time: O(n log n)** - Linearithmic time complexity. A sorting operation was detected. Most efficient comparison-based sorts (like quicksort, mergesort) run in O(n log n) time. This is efficient for most practical purposes.

**Space: O(1)** - Constant space complexity. The code uses a fixed amount of memory regardless of input size.
