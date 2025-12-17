# Sorting Singularly Nested Lists by Depth

You are given a list of lists, where each subarray can either be an empty list or contain one next nested list. Your task is to sort the main list in ascending order based on the depth of these subarrays.

## Input:

- You will receive an array of arrays (a list of lists).

- Each sub-array can only contain either another array or nothing (empty)

- Main array might be completely empty

## Understanding Depth

The depth is zero-based:

- The elements in the main array have depth 1.

- A single nested empty array (`[[]]`) has depth 2.

- A double-nested empty array (`[[[]]]`) has depth 3, and so on.

## Examples:

`[ [[[[[]]]]], [[]], [], [[[]]], []]`  -> `[ [], [], [[]], [[[]]], [[[[[]]]]] ]`

- `[]` has a depth of 1

- `[[]]` has a depth of 2

- `[[[]]]` has a depth of 3

- `[[[[[]]]]]` has a depth of 5

`[ [[]], [], [], [] , [[[[[[[]]]]]]], [], [[]] , [[[]]], [] ]`  -> `[ [], [], [], [], [], [[]], [[]], [[[]]], [[[[[[[]]]]]]] ]`

`[ [[]], [] ] -> [[], [[]] ]`

The final sorted order places the shallowest subarrays first and the deepest last.

# Given Code

```python
def sort_by_depth(arr):
    pass
```

# My Solution

```python
from typing import List, TypeAlias

# 1. Define the Recursive Type
# We define a type that is a list containing items of its own type.
# This represents: [], [[]], [[[]]], etc.
SingularNestedList: TypeAlias = list["SingularNestedList"]

def get_depth(nested_list: SingularNestedList) -> int:
    """
    Calculates the nesting depth of a singularly nested list.

    The depth is determined by peeling back layers until an empty list is found.
    - []       -> Depth 1
    - [[]]     -> Depth 2
    - [[[]]]   -> Depth 3

    Args:
        nested_list (SingularNestedList): The nested list to measure.

    Returns:
        int: The depth of the nesting (1-based).
    """
    depth: int = 1
    current: SingularNestedList = nested_list

    # Iterate while the current list is not empty
    while len(current) > 0:
        depth += 1
        # Move one layer deeper. We assume the list strictly contains
        # one item (the next list) based on problem constraints.
        current = current[0]
        
    return depth

def sort_by_depth(main_list: List[SingularNestedList]) -> List[SingularNestedList]:
    """
    Sorts a list of nested arrays in ascending order based on their depth.

    This function is stable and does not modify the original list in place
    if assigned to a new variable (though .sort() uses the reference).

    Args:
        main_list (List[SingularNestedList]): A list containing multiple nested lists.

    Returns:
        List[SingularNestedList]: The list sorted from shallowest to deepest.
    """
    # We use Python's built-in sort (Timsort) which is O(N log N).
    # We pass 'get_depth' as the key, so the sort is based on the integer returned by that function.
    main_list.sort(key=get_depth)
    
    return main_list
```

# Complexity Analysis

**Time Complexity:** O(n log n)

**Space Complexity:** O(n²)

**Explanation:**
**Time: O(n log n)** - Linearithmic time complexity. A sorting operation was detected. Most efficient comparison-based sorts (like quicksort, mergesort) run in O(n log n) time. This is efficient for most practical purposes.

**Space: O(n²)** - Quadratic space complexity. A 2D array or matrix structure was detected, requiring n × n memory allocation.
