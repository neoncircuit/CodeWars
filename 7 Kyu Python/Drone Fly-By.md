# Drone Fly-By

The other day I saw an amazing video where a guy hacked some wifi controlled lightbulbs by flying a drone past them. Brilliant.

In this kata we will recreate that stunt... sort of.

You will be given two strings: `lamps` and `drone`. `lamps` represents a row of lamps, currently off, each represented by `x`. When these lamps are on, they should be represented by `o`.

The drone string represents the position of the drone `T` (any better suggestion for character??) and its flight path up until this point `=`. The drone always flies left to right, and always begins at the start of the row of lamps. Anywhere the drone has flown, including its current position, will result in the lamp at that position switching on.

Return the resulting `lamps` string. See example tests for more clarity.

# Given Code

```python
def fly_by(lamps, drone):
    #hack the lamps
```

# My Solution

```python
def fly_by(lamps: str, drone: str) -> str:
    #hack the lamps
    n = min(len(drone), len(lamps))
    return 'o'*n + lamps[n:]
```

# Complexity Analysis

**Time Complexity:** O(1)

**Space Complexity:** O(1)

**Explanation:**
**Time: O(1)** - Constant time complexity. The code performs a fixed number of operations regardless of input size. No loops or recursive calls that depend on input size were detected.

**Space: O(1)** - Constant space complexity. The code uses a fixed amount of memory regardless of input size.
