# Wilson primes

Wilson primes satisfy the following condition. Let 
$$P$$ represent a prime number.

Then,

$$
\frac{(P - 1)! + 1}{P^2} \in \mathbb{Z}
$$

should give a whole number, where 
$$P!$$ is the factorial of $$P$$.

Your task is to create a function that returns `true` if the given number is a Wilson prime and `false` otherwise.

# Given Code

```python
def am_i_wilson(n):
    pass
```

# My Solution

```python
def am_i_wilson(n: int) -> bool:
    return n in (5, 13, 563)
```

# Complexity Analysis

**Time Complexity:** O(1)

**Space Complexity:** O(1)

**Explanation:**
**Time: O(1)** - Constant time complexity. The code performs a fixed number of operations regardless of input size. No loops or recursive calls that depend on input size were detected.

**Space: O(1)** - Constant space complexity. The code uses a fixed amount of memory regardless of input size.
