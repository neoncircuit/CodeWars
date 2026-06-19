# Filtering even numbers (Bug Fixes)

## Instructions

## Fix the bug in Filtering method

The method is supposed to remove even numbers from the list and return a list that contains the odd numbers.

However, there is a bug in the method that needs to be resolved.



## Given Code
```python
def kata_13_december(lst): 
    # Fix this code
    for i in range(len(lst)): 
        if lst[i]%2==0: 
            lst.remove(i)
    return lst
```

## My Solution
```python
def kata_13_december(lst): 
    # Fix this code
    return [i for i in lst if i % 2 != 0]
```
