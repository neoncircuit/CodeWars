# Sort Out The Men From Boys

## Scenario

Now that the competition gets tough it will Sort out the men from the boys .

Men are the Even numbers and Boys are the odd

# Given Code

```python
def men_from_boys(arr):
    #your code here
```

# My Solution

```python
def men_from_boys(arr: list[int]) -> list[int]:
    #your code here
    if not isinstance(arr, list):
        raise TypeError("Input must be a list.")
    
    unique_numbers = set(arr)  # Remove duplicates
    evens = sorted([x for x in unique_numbers if x % 2 == 0])
    odds = sorted([x for x in unique_numbers if x % 2 != 0], reverse=True)
    return evens + odds
```

# Complexity Analysis

**Time Complexity:** O(n log n)

**Space Complexity:** O(n)

**Explanation:**
**Time: O(n log n)** - Linearithmic time complexity. A sorting operation was detected. Most efficient comparison-based sorts (like quicksort, mergesort) run in O(n log n) time. This is efficient for most practical purposes.

**Space: O(n)** - Linear space complexity. Data structures (arrays, objects, sets, maps) were detected that may grow proportionally with input size.
