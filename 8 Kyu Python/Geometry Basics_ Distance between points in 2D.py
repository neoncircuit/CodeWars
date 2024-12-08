import math

def distance_between_points(a, b):
    # your code here
    x1, y1 = a.x, a.y
    x2, y2 = b.x, b.y
    x = math.pow(x2-x1, 2)
    y = math.pow(y2-y1, 2)
    return math.sqrt(x+y)