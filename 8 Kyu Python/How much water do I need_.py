def how_much_water(water : int, load : int, clothes : int) -> float:
    # Good luck!
    if clothes > 2 * load:
        return "Too much clothes"
    if clothes < load:
        return "Not enough clothes"
    
    extra_clothes = clothes - load
    total_water = water * (1.1 ** extra_clothes)
    
    return round(total_water, 2)