# pick a set of first elements

## Instructions

Write a function to get the first element(s) of a sequence. Passing a parameter `n` (default=`1`) will return the first `n` element(s) of the sequence.

If `n` == `0` return an empty sequence `[]`

## Examples

```
arr = ['a', 'b', 'c', 'd', 'e']
first(arr)    # --> ['a']
first(arr, 2) # --> ['a', 'b']
first(arr, 3) # --> ['a', 'b', 'c']
first(arr, 0) # --> []
```

## Given Code
```python
def first(seq, n): 
    # your code here
    pass
```

## My Solution
```python
def first(seq, n=1): 
    # your code here
    return seq[0:n] if seq else []
```
