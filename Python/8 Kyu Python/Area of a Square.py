import math

def square_area(A:int):
    # your code here
    r = (2 * A) / math.pi 
    area = math.pow(r, 2)
    return round(area, 2)