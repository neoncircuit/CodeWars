# Circles in Polygons

You are the owner of a box making company.

Your company can produce any equal sided polygon box, but plenty of your customers want to transport circular objects in these boxes. Circles are a very common shape in the consumer industry. Tin cans, glasses, tyres and CD's are a few examples of these.

As a result you decide to add this information on your boxes: The largest (diameter) circular object that can fit into a given box.

# Given Code

```{python}
def circle_diameter(sides, side_length): 
    # your code here
    pass
```

# My Solution

```{python}
from math import tan, pi

def circle_diameter(sides, side_length): 
    """
    This function calculates the largest diameter of a circle that can fit inside a polygon with given number of sides and side length.
    
    Args:
    sides (int): Number of sides of the polygon.
    side_length (float): Length of each side of the polygon.
    
    Returns:
    float: Largest diameter of a circle that can fit inside the polygon.
    """
    # Calculate the apothem of the polygon using the formula: apothem = side_length / (2 * tan(pi/sides))
    apothem = side_length / (2 * tan(pi/sides))
    
    # Calculate the diameter of the circle using the formula: 2 * apothem
    return 2 * apothem
```
