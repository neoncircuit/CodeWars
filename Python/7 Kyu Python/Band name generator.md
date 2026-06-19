# Band name generator

My friend wants a new band name for her band. She like bands that use the formula: "The" + a noun with the first letter capitalized, for example:

`"dolphin" -> "The Dolphin"`

However, when a noun STARTS and ENDS with the same letter, she likes to repeat the noun twice and connect them together with the first and last letter, combined into one word (WITHOUT "The" in front), like this:

`"alaska" -> "Alaskalaska"`

Complete the function that takes a noun as a string, and returns her preferred band name written as a string.

# Given Code

```python
def band_name_generator(name):
    pass
```

# My Solution

```python
def band_name_generator(name: str) -> str:
    if name[0] == name[-1]:
        return f"{name.capitalize()}{name[1:]}"
    else:
        return f"The {name.capitalize()}"
```

# Complexity Analysis

**Time Complexity:** O(1)

**Space Complexity:** O(1)

**Explanation:**
**Time: O(1)** - Constant time complexity. The code performs a fixed number of operations regardless of input size. No loops or recursive calls that depend on input size were detected.

**Space: O(1)** - Constant space complexity. The code uses a fixed amount of memory regardless of input size.
