import math

def db_scale(intensity: int) -> float:
    # Your code here
    decibel: float = 10 * math.log10(intensity/10**-12)
    return decibel