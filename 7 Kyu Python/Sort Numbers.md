# Sort Numbers
Finish the solution so that it sorts the passed in array of numbers. If the function passes in an empty array or null/nil value then it should return an empty array.

## Example: (input --> output)

```
solution([1,2,3,10,5]) # should return [1,2,3,5,10]
solution(None) # should return []
```

# Given Code

```{python}
def solution(nums):
    pass
```

# My Solution

```{python}
def solution(nums):
    if nums is None or len(nums) == 0:
        return []
    else:
        sortedNums = sorted(nums)
        return sortedNums
```
