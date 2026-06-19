def ice_brick_volume(radius: int, bottle_length: int, rim_length: int) -> int:
    while (radius > 0 and bottle_length > 0 and rim_length < bottle_length): 
        brick_height = bottle_length - rim_length
        return 2 * radius**2 * brick_height