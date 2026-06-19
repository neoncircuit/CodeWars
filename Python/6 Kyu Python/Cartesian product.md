# Cartesian product

The **cartesian product** of two sets A and B, written **"A × B"** is equal to the set of all possible combinations of values from both sets. Here's an example, taken from [Mathstopia](https://www.mathstopia.net/sets/cartesian-product) :

![](https://www.mathstopia.net/wp-content/uploads/2021/01/cartesian-products.jpg)

## Your task
Implement function `cart_prod`, which returns the cartesian product (in the form of `tuples`) of any number of sets passed to it (note the * before `sets` in the function definition). Also,

- The cartesian product A × B × C, where A, B and C are sets, is equal to (A × B) × C. See bottom of description for a concrete e×ample.
- If no set is passed in, return a set containing an tempty tuple.
- If a single set is passed in, return a set of tuples of the elements of the set.
- If any of the sets passed in is empty, return an empty set.

Note : You are not allowed to use the word "itertools" in your solution (as in, `from itertools import product ¯\(ツ)/¯`).

## Example with three sets
If `A = {1, 2}; B = {'x', 'y'}; C = {δ, γ}` Then `A × B × C = {(1, 'x', δ), (1, 'x', γ), (1, 'y', δ), (1, 'y', γ), (2, 'x', δ), (2, 'x', γ), (2, 'y', δ), (2, 'y', γ)}` 

Note that the cardinality (number of elements) of a cartesian product is always equal to the product of the cardinalities of the sets in the cartesian product (here, |A| = |B| = |C| = 2, therefore |A × B × C| = 8).

# Given Code

```python
def cart_prod(*sets):
    return # the cartesian product of the sets
```

# My Solution

```python
def cart_prod(*sets):
    """
    Return the Cartesian product of input iterables as a set of tuples.

    Args:
        *sets: One or more iterables whose Cartesian product will be computed.

    Returns:
        A set of tuples representing the Cartesian product.
    """
    if not sets:
        return {()}
    result = {()}
    for s in sets:
        result = {r + (x,) for r in result for x in s}
    return result
```

# Complexity Analysis

**Time Complexity:** O(n)

**Space Complexity:** O(1)

**Explanation:**
**Time: O(n)** - Linear time complexity. The code iterates through the input once (using loops like for, while, forEach, map, filter, reduce). The number of operations grows proportionally with the input size.

**Space: O(1)** - Constant space complexity. The code uses a fixed amount of memory regardless of input size.
