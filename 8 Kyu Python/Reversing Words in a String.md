# Reversing Words in a String

## Instructions

You need to write a function that reverses the words in a given string. Words are always separated by a single space.

As the input may have trailing spaces, you will also need to ignore unneccesary whitespace.

## Example (Input --> Output)

```
"Hello World" --> "World Hello"
"Hi There." --> "There. Hi"
```

Happy coding!

## Given Code
```python
def reverse(st):
    # Your Code Here
    return st
```

## My Solution
```python
def reverse(st):
    # Your Code Here
    return " ".join(st.split()[::-1])
```
