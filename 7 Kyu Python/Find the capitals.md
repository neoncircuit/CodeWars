# Find the capitals

## Instructions

## Instructions

Write a function that takes a single non-empty string of only lowercase and uppercase ascii letters (`word`) as its argument, and returns an ordered list containing the indices of all capital (uppercase) letters in the string.

## Example (Input --> Output)

```
"CodEWaRs" --> [0,3,4,6]
```

## Given Code
```python
def capitals(word):
    #your code here
```

## My Solution
```python
def capitals(word):
    #your code here
    res = [idx for idx in range(len(word)) if word[idx].isupper()]
    return res
```
