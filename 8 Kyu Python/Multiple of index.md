# Multiple of index

## Instructions

Return a new array consisting of elements which are multiple of their own index in input array (length > 1).

## Some cases:
```
[22, -6, 32, 82, 9, 25] =>  [-6, 32, 25]

[68, -1, 1, -7, 10, 10] => [-1, 10]

[-56,-85,72,-26,-14,76,-27,72,35,-21,-67,87,0,21,59,27,-92,68] => [-85, 72, 0, 68]
```

## Given Code
```python
def multiple_of_index(arr):
    pass
```

## My Solution
```python
def multiple_of_index(arr):
    result = []
    for i in range(len(arr)): 
        if i == 0: 
            if arr[i] == 0:
                result.append(arr[i])
        elif arr[i] % i == 0:
            result.append(arr[i])
    return result
```
