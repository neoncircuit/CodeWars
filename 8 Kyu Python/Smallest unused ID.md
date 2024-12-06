# Smallest unused ID

## Instructions

Hey awesome programmer!

You've got much data to manage and of course you use zero-based and non-negative ID's to make each data item unique!

Therefore you need a method, which returns the smallest unused ID for your next new data item...

Note: The given array of used IDs may be unsorted. For test reasons there may be duplicate IDs, but you don't have to find or remove them!

Go on and code some pure awesomeness!

## Given Code
```python
def next_id(arr):
    #your code here
```

## My Solution
```python
def next_id(arr):
    #your code here
    current = 0
    while current in arr:
        current += 1
    return current
```
