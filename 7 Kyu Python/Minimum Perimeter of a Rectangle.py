import math

def minimum_perimeter(area: int) -> int:
    if area < 1:
        raise ValueError("area must be >= 1")

    root = math.isqrt(area)
    perimeter_root = None
    perimeter_reg = None

    if math.pow(root, 2) == area:
        perimeter_root = 4 * root

    for height in range(root, 0, -1):
        if area % height == 0:
            width = area // height
            if height != width:
                perimeter_reg = 2 * (height + width)
                break  

    if perimeter_root is not None and perimeter_reg is not None:
        return min(perimeter_root, perimeter_reg)
    elif perimeter_root is not None:
        return perimeter_root
    elif perimeter_reg is not None:
        return perimeter_reg
    else: 
        return 4