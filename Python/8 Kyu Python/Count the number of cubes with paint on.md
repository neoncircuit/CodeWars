# Count the number of cubes with paint on

Upon arriving at an interview, you are presented with a solid blue cube. The cube is then dipped in red paint, coating the entire surface of the cube. The interviewer then proceeds to cut through the cube in all three dimensions a certain number of times.

Your function takes as parameter the number of times the cube has been cut. You must return the number of smaller cubes created by the cuts that have at least one red face.

To make it clearer, the picture below represents the cube after (from left to right) 0, 1 and 2 cuts have been made.

![alt text](https://i.imgur.com/36x8Fkv.png)

# Given Code

```{python}
def count_squares(cuts):
    pass
```

# My Solution

```{python}
def count_squares(cuts):
    # The function calculates the total number of smaller cubes with at least one red face
    # after making a specified number of cuts on each dimension of an originally larger cube
    # with all external faces painted red.

    # The formula to calculate this is derived based on the arrangement of smaller cubes:
    # - 8 corners are always exposed on any cube, each contributing one red-faced smaller cube.
    # - Edges (excluding corners) contribute smaller cubes, with each of the 12 edges giving
    #   (cuts - 1) red-faced smaller cubes. The (cuts - 1) accounts for the ends of each edge
    #   not being counted again (already counted as corners).
    # - Faces (excluding edges) contribute, with each of the 6 faces giving (cuts - 1)^2
    #   red-faced smaller cubes. The (cuts - 1)^2 accounts for the perimeter of each face
    #   not being counted again (as those are part of edges).

    # Total red-faced smaller cubes:
    return 8 + 12 * (cuts-1) + 6 * pow(cuts-1, 2)
```
