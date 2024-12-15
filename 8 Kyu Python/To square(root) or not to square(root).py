import math

def square_or_square_root(arr):
    result = []
    for i in arr:
        if math.isqrt(i)**2 == i:
            result.append(math.isqrt(i))  
        else:
            result.append(i**2) 
    return result