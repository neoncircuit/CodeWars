from math import sqrt, floor, ceil

def nearest_sq(n):
    # pass
    f = floor(sqrt(n))
    c = ceil(sqrt(n))
    
    upper = c ** 2
    lower = f ** 2
    
    if abs(upper - n) < abs(lower - n):
        return upper
    else:
        return lower
