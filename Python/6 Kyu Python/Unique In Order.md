# Unique In Order

## Instructions

Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

For example:

```
unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]
```

## Given Code
```python
def unique_in_order(sequence):
    return
```

## My Solution
```python
def unique_in_order(sequence):
    result = []
    for i, char in enumerate(sequence):
        # Add the first character or if it's different from the previous one
        if i == 0 or char != sequence[i - 1]:
            result.append(char)
    return result
```
