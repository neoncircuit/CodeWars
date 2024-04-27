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
