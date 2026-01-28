# Grasshopper - Messi goals function

![Messi](https://en.wikipedia.org/wiki/Lionel_Messi) is a soccer player with goals in three leagues:

- LaLiga
- Copa del Rey
- Champions

Complete the function to return his total number of goals in all three leagues.

Note: the input will always be valid.

For example:
```
5, 10, 2  -->  17
```

# Given Code

```python
def goals(laLiga, copaDelRey, championsLeague):
    pass
```

# My Solution

```python
def goals(laLiga: int, copaDelRey: int, championsLeague: int) -> int:
    """
    Return the total number of Messi's goals in all 3 leagues.
    
    Args:
        - laLiga: int - Number of Messi goals scored in the LaLiga league
        - copaDelRey: int - Number of Messi goals scored in the Copa del Rey league
        - championsLeague: int - Number of Messi goals scored in the Champions league
    
    Returns:
        Total number of goals that Messi scored
    """
    return sum([laLiga, copaDelRey, championsLeague])
```

# Complexity Analysis

**Time Complexity:** O(1)

**Space Complexity:** O(1)

**Explanation:**
**Time: O(1)** - Constant time complexity. The code performs a fixed number of operations regardless of input size. No loops or recursive calls that depend on input size were detected.

**Space: O(1)** - Constant space complexity. The code uses a fixed amount of memory regardless of input size.
