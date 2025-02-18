# Maximum Length Difference

## Instructions

You are given two arrays `a1` and `a2` of strings. Each string is composed with letters from `a` to `z`. Let `x` be any string in the first array and y be any string in the second array.

`Find max(abs(length(x) − length(y)))`

If `a1` and/or `a2` are empty return `-1` in each language except in Haskell (F#) where you will return `Nothing` (None).

## Example:

```
a1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
a2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
mxdiflg(a1, a2) --> 13
```

## Bash note:

- input : 2 strings with substrings separated by `,`

- output: number as a string

## Given Code
```python
def mxdiflg(a1, a2):
    # your code
    return -1
```

## My Solution
```python
def mxdiflg(a1, a2):
    # your code
    if not a1 or not a2:
        return -1
    
    length_a1 = [len(s) for s in a1]
    length_a2 = [len(s) for s in a2]
    
    max_a1 = max(length_a1)
    min_a1 = min(length_a1)
    max_a2 = max(length_a2)
    min_a2 = min(length_a2)
    
    return max(max_a1 - min_a2, max_a2 - min_a1)
```
