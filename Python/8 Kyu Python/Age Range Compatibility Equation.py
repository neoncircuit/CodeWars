import math

def dating_range(age):
    while 1 <= age <= 100:
        if age <= 14:
            min = age - 0.10 * age
            max = age + 0.10 * age
        else:
            min = (age/2) + 7
            max = (age-7) * 2
        return f"{math.floor(min)}-{math.floor(max)}"