# Is it a palindrome?

## Instructions

Write a function that checks if a given string (case insensitive) is a palindrome.

A palindrome is a word, number, phrase, or other sequence of symbols that reads the same backwards as forwards, such as `madam` or `racecar`.

## Given Code
```python
def is_palindrome(s):
    return
```

## My Solution
```python
def is_palindrome(s) -> bool:
    return True if s.lower() == s.lower()[::-1] else False
```
