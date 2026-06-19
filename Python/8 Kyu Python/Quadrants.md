# Quadrants

## Task
Given a point in a Euclidean plane (x and y), return the quadrant the point exists in: 1, 2, 3 or 4 (integer). x and y are non-zero integers, therefore the given point never lies on the axes.

## Examples
(1, 2)     => 1
(3, 5)     => 1
(-10, 100) => 2
(-1, -9)   => 3
(19, -56)  => 4

![Reference](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Cartesian_coordinates_2D.svg/300px-Cartesian_coordinates_2D.svg.png)

# Given Code

```{python}
def quadrant(x, y):
    # Poveli!
    pass
```

# My Solution

```{python}
def quadrant(x, y):
    # Poveli!
    match (x>0, y>0):
        case (True, True):
            return 1
        case (False, True):
            return 2
        case (False, False):
            return 3
        case (True, False):
            return 4
```
