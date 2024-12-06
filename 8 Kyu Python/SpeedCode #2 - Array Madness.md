# SpeedCode #2 - Array Madness

## Instructions

## Objective

Given two integer arrays a, b, both of length >= 1, create a program that returns true if the sum of the squares of each element in a is strictly greater than the sum of the cubes of each element in b.

E.g.

```
array_madness([4, 5, 6], [1, 2, 3]) => True #because 4 ** 2 + 5 ** 2 + 6 ** 2 > 1 ** 3 + 2 ** 3 + 3 ** 3
```

Get your timer out. Are you ready? Ready, get set, GO!!!

## Given Code
```python
def array_madness(a,b):
    # Ready, get, set, GO!!!
```

## My Solution
```python
def array_madness(a,b):
    # Ready, get, set, GO!!!
    sumA = sum(i ** 2 for i in a)
    sumB = sum(j ** 3 for j in b)
    return True if sumA > sumB else False
```
