import math

def volume(r:int, h:int):
    # Volume of cone is pi*r*(h/3)
    return int(math.pi * math.pow(r, 2) * (h/3))
