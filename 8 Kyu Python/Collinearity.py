def collinearity(x1, y1, x2, y2):
    determinant = x1 * y2 - y1 * x2
    return determinant == 0
