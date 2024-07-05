def zero_fuel(distance_to_pump, mpg, fuel_left):
    #Happy Coding! ;)
    mileage = mpg * fuel_left
    if mileage >= distance_to_pump:
        return True
    else: 
        return False
