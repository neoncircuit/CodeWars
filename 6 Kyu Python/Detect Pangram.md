# Detect Pangram

## Instructions

A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

## Given Code
```python
def is_pangram(st):
    return False
```

## My Solution
```python
import string

def is_pangram(st):
    # Create a set of all lowercase alphabetic characters
    alphabet = set(string.ascii_lowercase)
    
    # Normalize input: lowercase and filter alphabetic characters
    s_letters = set(c.lower() for c in st if c.isalpha())
    
    # Check if the input contains all the letters in the alphabet
    return alphabet.issubset(s_letters)
```
