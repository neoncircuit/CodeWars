# Is there a vowel in there?

## Instructions

Given an array of numbers, check if any of the numbers are the character codes for lower case vowels (`a, e, i, o, u`).

If they are, change the array value to a string of that vowel.

Return the resulting array.

## Given Code
```python
def is_vow(inp):
    pass
```

## My Solution
```python
def is_vow(inp):
    vowels = {97: 'a', 101: 'e', 105: 'i', 111: 'o', 117: 'u'}
    result = []
    for num in inp:
        if num in vowels:
            result.append(vowels[num])
        else:
            result.append(num)  
    return result
```
