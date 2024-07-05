# Square(n) Sum

Complete the square sum function so that it squares each number passed into it and then sums the results together.

For example, for [1, 2, 2] it should return 9 because 
1<sup>2</sup> + 2<sup>2</sup> + 2<sup>2</sup> = 9

# Given Code

```{python}
def square_sum(numbers):
    #your code here
```

# My Solution

```{python}
def square_sum(numbers):
    #your code here
    sum = 0
    for i in numbers:
        sum += i * i
    return sum
```
