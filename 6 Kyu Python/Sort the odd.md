# Sort the odd

## Task
You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

## Examples
```
[7, 1]  =>  [1, 7]
[5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]
```

# Given Code

```{python}
def sort_array(source_array):
    # Return a sorted array.
```

# My Solution

```{python}
def sort_array(source_array):
    # Create two empty lists for odd and even numbers
    odd_nums = []
    even_nums = []

    # Iterate through the source array and add odd and even numbers to their respective lists
    for i in source_array:
        if i % 2 != 0:
            odd_nums.append(i)
        else:
            even_nums.append(i)

    # Sort the odd numbers list in ascending order
    odd_nums.sort()

    # Create a new list by iterating through the source array and replacing odd numbers with the next number in the sorted odd_nums list
    sorted_array = []
    for num in source_array:
        if num % 2 != 0:
            sorted_array.append(odd_nums.pop(0))
        else:
            sorted_array.append(num)

    return sorted_array

```
