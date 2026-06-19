# Name Shuffler

## Instructions

Write a function that returns a string in which firstname is swapped with last name.

## Example(Input --> Output)

```
"john McClane" --> "McClane john"
```

## Given Code
```python
def name_shuffler(str_):
    #your code here
```

## My Solution
```python
def name_shuffler(str_):
    #your code here
    return " ".join(str_.split()[::-1])
```
