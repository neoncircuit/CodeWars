# What's the real floor?

## Instructions

Americans are odd people: in their buildings, the first floor is actually the ground floor and there is no 13th floor (due to superstition).

Write a function that given a floor in the american system returns the floor in the european system.

With the 1st floor being replaced by the ground floor and the 13th floor being removed, the numbers move down to take their place. In case of above 13, they move down by two because there are two omitted numbers below them.

Basements (negatives) stay the same as the universal level.

[More Information Here](https://en.wikipedia.org/wiki/Storey#European_scheme)

## Examples

```
1  =>  0 
0  =>  0
5  =>  4
15  =>  13
-3  =>  -3
```

## Given Code
```python
def get_real_floor(n):
    # code here
```

## My Solution
```python
def get_real_floor(n):
    # code here
    while n != 13:
        return n if n < 0 else 0 if n < 2 else n-1 if n < 14 else n-2
```
