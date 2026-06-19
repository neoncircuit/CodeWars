# Enumerable Magic #4 - True for None?

Write a function that takes two arguments: an array and a callback function (in Ruby: a block).

The function should return `true` if the callback / block returns `false` for all of the items in the array, or if the array is empty; otherwise return `false`.

# Given Code

```python
def none(lst, func):
    pass
```

# My Solution

```python
def none(lst: list[int], func) -> bool:
    """
    Return True if no element in the list satisfies the predicate.

    Check whether the predicate function `func` returns False for every element
    in `lst`. If the list is empty, returns True.

    Args:
        - lst: list[int]: A list of integers to test.
        - func: callable: A predicate that accepts an int and returns a bool.
                          If func(x) is True for any element x, this function
                          returns False. Remember to import typing when using this.

    Returns:
        bool: True if `func` returns False for all elements in `lst` (or if
              `lst` is empty). Returns False if `func` returns True for at
              least one element.

    Examples:
        >>> none([0, 1, 2], lambda x: x > 100)
        True
        >>> none([], lambda x: x == 0)
        True
        >>> none([1, 2, 3], lambda x: x % 2 == 0)
        False
    """
    for x in lst:
        if func(x):
            return False
    return True
```

# Complexity Analysis

**Time Complexity:** O(n)

**Space Complexity:** O(n)

**Explanation:**
**Time: O(n)** - Linear time complexity. The code iterates through the input once (using loops like for, while, forEach, map, filter, reduce). The number of operations grows proportionally with the input size.

**Space: O(n)** - Linear space complexity. Recursion was detected, which uses call stack space proportional to the recursion depth.
