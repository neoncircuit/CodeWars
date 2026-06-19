# Aspect Ratio Cropping - Part 1

The aspect ratio of an image describes the proportional relationship between its width and its height. Most video shown on the internet uses a 16:9 aspect ratio, which means that for every pixel in the Y, there are roughly 1.77 pixels in the X (where 1.77 ~= 16/9). As an example, 1080p video with an aspect ratio of 16:9 would have an X resolution of 1920, however 1080p video with an aspect ratio of 4:3 would have an X resolution of 1440.

Write a function that accepts arbitrary X and Y resolutions and converts them into resolutions with a 16:9 aspect ratio that maintain equal height. Round your answers up to the nearest integer.

This kata is part of a series with [Aspect Ratio Cropping - Part 2](https://www.codewars.com/kata/aspect-ratio-cropping-part-2) .

## Example
374 × 280 pixel image with a 4:3 aspect ratio.
![](https://upload.wikimedia.org/wikipedia/commons/4/43/Aspect_ratio_4_3_example.jpg)

500 × 280 pixel image with a 16:9 aspect ratio.
![](https://upload.wikimedia.org/wikipedia/commons/2/2c/Aspect_ratio_16_9_example3.jpg)

# Given Code

```python
from typing import Tuple


def aspect_ratio(x: int, y: int) -> Tuple[int, int]:
    # 頑張って！
    pass
```

# My Solution

```python
from typing import Tuple
import math

def aspect_ratio(x: int, y: int) -> Tuple[int, int]:
    # 頑張って！
    target_aspect_ratio: float = 16/9
    new_x : int = math.ceil(y * target_aspect_ratio)
    new_y: int = y
    return (new_x, new_y)
```

# Complexity Analysis

**Time Complexity:** O(1)

**Space Complexity:** O(1)

**Explanation:**
**Time: O(1)** - Constant time complexity. The code performs a fixed number of operations regardless of input size. No loops or recursive calls that depend on input size were detected.

**Space: O(1)** - Constant space complexity. The code uses a fixed amount of memory regardless of input size.
