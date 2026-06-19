# Remove All The Marked Elements of a List

Define a method/function that removes from a given array of integers all the values contained in a second array.

## Examples (input -> output):
```
* [1, 1, 2, 3, 1, 2, 3, 4], [1, 3] -> [2, 2, 4]
* [1, 1, 2, 3, 1, 2, 3, 4, 4, 3, 5, 6, 7, 2, 8], [1, 3, 4, 2] -> [5, 6, 7, 8]
* [8, 2, 7, 2, 3, 4, 6, 5, 4, 4, 1, 2, 3], [2, 4, 3] -> [8, 7, 6, 5, 1]
```

Enjoy it!!

# Given Code

```python
class List:
    def remove_(self, integer_list, values_list):
        return []
```

# My Solution

```python
class List:
    def remove_(self, integer_list: list[int], values_list: list[int]) -> list[int]:
        remove_ints = set(values_list)
        found = any(num in remove_ints for num in integer_list)
        integer_list[:] = [num for num in integer_list if num not in remove_ints]
        return integer_list
```

# Complexity Analysis

**Time Complexity:** O(n)

**Space Complexity:** O(n)

**Explanation:**
**Time: O(n)** - Linear time complexity. The code iterates through the input once (using loops like for, while, forEach, map, filter, reduce). The number of operations grows proportionally with the input size.

**Space: O(n)** - Linear space complexity. Data structures (arrays, objects, sets, maps) were detected that may grow proportionally with input size.
