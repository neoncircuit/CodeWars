import math

def find_slope(points: list[int]) -> str:
    a, b, c, d = points
    try: 
        m: int = math.floor((d - b)/(c - a))
        return str(m)
    except ZeroDivisionError:
        return "undefined"