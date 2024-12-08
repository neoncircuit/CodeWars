# Do you speak "English"?

## Instructions

Given a string of arbitrary length with any ascii characters. Write a function to determine whether the string contains the whole word "English".

The order of characters is important -- a string "abcEnglishdef" is correct but "abcnEglishsef" is not correct.

Upper or lower case letter does not matter -- "eNglisH" is also correct.

Return value as boolean values, true for the string to contains "English", false for it does not.

## Given Code
```python
def sp_eng(sentence): 
    # your code here
    pass
```

## My Solution
```python
def sp_eng(sentence): 
    # your code here
    return "english" in sentence.lower()
```
