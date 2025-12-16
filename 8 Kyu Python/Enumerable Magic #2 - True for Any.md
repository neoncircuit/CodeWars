# Enumerable Magic #2 - True for Any?

The task is to write a function that accepts two parameters: an array and a callback function (in Ruby: a block).

The function should return true if the callback function / block returns `true` for any item in the array, otherwise return `false`.

The function should return `false` if the array is empty.

# Given Code

```python
def any_(lst, func): 
    pass
```

# My Solution

```python
from typing import Callable, List, TypeVar, Any

def any_(lst: List[Any], func: Callable[[Any], bool]) -> bool: 
    """
    Check if func returns True for any item in the array
    
    Args:
        lst: typing.List[Any]
        func: typing.Callable[[Any], bool]
    
    Returns: 
        True if the callback returns True for ANY item.
        False if the list is empty or no items match.
    """
    for item in lst:
        if func(item):
            return True
            
    return False
```

# Time Complexity

O(n)
