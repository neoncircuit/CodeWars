# No zeros for heros

## Instructions

Numbers ending with zeros are boring.

They might be fun in your world, but not here.

Get rid of them. Only the ending ones.

```
1450 -> 145
960000 -> 96
1050 -> 105
-1050 -> -105
```

Zero alone is fine, don't worry about it. Poor guy anyway



## Given Code
```python
def no_boring_zeros(n):
    # your code
```

## My Solution
```python
def no_boring_zeros(n):
    # your code
    while n % 10 == 0 and n != 0:
        n //= 10  
    return n
```
