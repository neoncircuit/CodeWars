# String Scramble

Given a string and an array of indices, rearrange the characters of the string so that each character is placed at the position specified by the corresponding index in the array.

## Example

```
input: "abcd", [0, 3, 1, 2]
output: "acdb"
```

## Explanation
- The character `'a'` is placed at index `0`.

- The character `'b'` is placed at index `3`.

- The character `'c'` is placed at index `1`.

- The character `'d'` is placed at index `2`.

## Notes
- The string and the array will be of equal length.

- The string will contain valid characters (A-Z, a-z, or 0-9);
the array will contain valid indices.

# Given Code

```python
def scramble(strng, array):
    pass
```

# My Solution

```python
def scramble(strng: str, array: list[int]) -> str:
    result_list = [''] * len(strng)
    
    for char, index in zip(strng, array):
        result_list[index] = char
        
    return "".join(result_list)
```

# Complexity Analysis

**Time Complexity:** O(1)

**Space Complexity:** O(n)

**Explanation:**
**Time: O(1)** - Constant time complexity. The code performs a fixed number of operations regardless of input size. No loops or recursive calls that depend on input size were detected.

**Space: O(n)** - Linear space complexity. Data structures (arrays, objects, sets, maps) were detected that may grow proportionally with input size.
