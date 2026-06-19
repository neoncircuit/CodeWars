# Find the position!

## Instructions

When provided with a letter, return its position in the alphabet.

Input :: "a"

Output :: "Position of alphabet: 1"

**Note: Only lowercased English letters are tested**

## Given Code
```python
def position(letter):
    pass
```

## My Solution
```python
def position(letter):
    letter = letter.lower()
    if 'a' <= letter <= 'z':
        return f"Position of alphabet: {ord(letter) - ord('a') + 1}"
    else:
        return None
```
