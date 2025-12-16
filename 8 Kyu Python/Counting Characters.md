# Counting Characters

Define a method named `countCharOccurrences` or `count_char_occurrences` that accepts a string and a char as inputs and returns the number of times the char occurs in the string as an int.

# Given Code

```python
def count_char_occurrences(strng, char):
    pass
```

# My Solution

```python
def count_char_occurrences(string_input: str, char_input: chr) -> int:
    """
    Given an input string and char 
    Find the number of occurrences of the char input inside the string input
    
    args:
        string_input: str
        char_input: chr
    
    returns:
        int
    """
    return string_input.count(char_input)
```

# Time Complexity

O(1)
