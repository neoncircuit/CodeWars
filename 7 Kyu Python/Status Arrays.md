# Status Arrays

The status of each element of an array of integers can be determined by its position in the array and the value of the other elements in the array. The status of an element E in an array of size N is determined by adding the position P, 0 <= P < N, of the element in the array to the number of array elements in the array that are less than E.

For example, consider the array containing the integers: 6 9 3 8 2 3 1. The status of the element 8 is 8 because its position is 3 and there are 5 elements in the array that are less than 8.

You will return the elements of the original array from low to high status order. In the event there is a tie for status of two or more elements, you will output them in order of appearance in the array.

## EXAMPLE:
```
status([6, 9, 3, 8, 2, 3, 1]) = [6, 3, 2, 1, 9, 3, 8]
```

# Given Code

```python
def status(nums):
    #let's crank some code!
```

# My Solution

```python
def status(nums: list[int]) -> list[int]:
    #let's crank some code!
    # Step 1. Sort the list of integers
    nums_sorted = sorted(nums)
    
    # Step 2. Map the value, how many numbers are smaller than the target number
    value_to_count_less = {}
    for idx, v in enumerate(nums_sorted):
        if v not in value_to_count_less:
            value_to_count_less[v] = idx
            
    # Step 3. Iterate original array and compute status for each element
    triples = []  # (status, original_index, value)
    for i, v in enumerate(nums):
        count_less = value_to_count_less[v]
        status = i + count_less
        triples.append((status, i, v))
        print(f"index={i}, value={v}, count_less={count_less}, status={status}")

    # Step 4. Sort by status then original index (tuples sort that way by default)
    triples.sort()

    # Step 5. Extract values in the new order
    return [v for _, _, v in triples]
```

# Complexity Analysis

**Time Complexity:** O(n log n)

**Space Complexity:** O(n)

**Explanation:**
**Time: O(n log n)** - Linearithmic time complexity. A sorting operation was detected. Most efficient comparison-based sorts (like quicksort, mergesort) run in O(n log n) time. This is efficient for most practical purposes.

**Space: O(n)** - Linear space complexity. Data structures (arrays, objects, sets, maps) were detected that may grow proportionally with input size.
