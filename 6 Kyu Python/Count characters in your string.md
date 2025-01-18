# Count characters in your string

## Instructions

The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be `{'a': 2, 'b': 1}`.

What if the string is empty? Then the result should be empty object literal, `{}`.

## Given Code
```python
def count(s):
    # The function code should be here
    return {s.count('a'), s.count('b')}
```

## My Solution
```python
def count(s):
    # The function code should be here
    dict = {}
    
    for letter in s:
        if letter in dict:
            dict[letter] += 1
        else: 
            dict[letter] = 1
    
    return dict
```
