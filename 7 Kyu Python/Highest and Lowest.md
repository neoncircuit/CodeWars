# Highest and Lowest

In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

## Examples
```
high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"
```

## Notes
All numbers are valid Int32, no need to validate them.
There will always be at least one number in the input string.
Output string must be two numbers separated by a single space, and highest number is first.

# Given Code

```{python}
def high_and_low(numbers):
    # ...
    return numbers
```

# My Solution

```{python}
def high_and_low(numbers):
    numlist = numbers.split(" ")
    i = 0
    highest = int(numlist[0])
    lowest = int(numlist[0])
    while i < len(numlist):
        numlist[i] = int(numlist[i])
        if numlist[i] > highest:
            highest = numlist[i]
        if numlist[i] < lowest:
            lowest = numlist[i]
        i += 1
    highest = str(highest)
    lowest = str(lowest)
    return  highest+" "+lowest
```

# My Solution 2

```{python}
def high_and_low(numbers):
    # ...
    # return numbers
    nums = [int(i) for i in numbers.split()]
    return " ".join([str(max(nums)), str(min(nums))])
```
