import math

def roots(a:int, b:int, c:int):
    discriminant = math.pow(b, 2) - 4*a*c
    
    # return None if discriminant is negative, 
    # otherwise sum of roots is always -b/a regardless of discriminant
    return None if discriminant < 0 else round(-b/a, 2) 