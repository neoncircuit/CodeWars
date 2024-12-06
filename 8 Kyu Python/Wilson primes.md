# Wilson primes

## Instructions

**Wilson primes** satisfy the following condition. Let *P* represent a prime number.

Then:

$$\frac{(P - 1)! + 1}{P * P}$$

should give a whole number, where *P*! is the factorial of *P*.

Your task is to create a function that returns `true` if the given number is a Wilson prime and `false` otherwise.

## Given Code
```python
def am_i_wilson(n):
    pass
```

## My Solution
```python
def am_i_wilson(n):
    # Wilson primes are only 2, 3, 5
    return n in [2, 3, 5]
```
