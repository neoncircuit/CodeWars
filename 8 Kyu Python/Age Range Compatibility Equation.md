# Age Range Compatibility Equation

## Instructions

Everybody knows the classic "half your age plus seven" dating rule that a lot of people follow (including myself). It's the 'recommended' age range in which to date someone.

![Alt text](http://web.archive.org/web/20190206114947if_/http://weknowmemes.com/wp-content/uploads/2014/08/age-range-compatibility-equation.jpg)

`minimum age <= your age <= maximum age`

## Task

Given an integer (1 <= n <= 100) representing a person's age, return their minimum and maximum age range.

This equation doesn't work when the age <= 14, so use this equation instead:

```
min = age - 0.10 * age
max = age + 0.10 * age
```

You should floor all your answers so that an integer is given instead of a float (which doesn't represent age). `Return your answer in the form [min]-[max]`

## Examples:

```
age = 27   =>   20-40
age = 5    =>   4-5
age = 17   =>   15-20
```

## Given Code
```python
def dating_range(age):
    pass
```

## My Solution
```python
import math

def dating_range(age):
    while 1 <= age <= 100:
        if age <= 14:
            min = age - 0.10 * age
            max = age + 0.10 * age
        else:
            min = (age/2) + 7
            max = (age-7) * 2
        return f"{math.floor(min)}-{math.floor(max)}"
```
