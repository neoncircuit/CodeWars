# Are arrow functions odd?

## Instructions

Time to test your basic knowledge in functions! Return the odds from a list:

```
[1, 2, 3, 4, 5]  -->  [1, 3, 5]
[2, 4, 6]        -->  []
```

## Given Code
```python
odds = lambda: 
```

## My Solution
```python
odds = lambda arr: list(filter(lambda x: x % 2 != 0, arr))
```
