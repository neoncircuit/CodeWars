def cube_checker(volume, side):
    while side > 0:
        cube = pow(side, 3)
        if cube == volume:
            return True
        break
    return False
