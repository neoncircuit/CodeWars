def quadrant(x, y):
    # Poveli!
    match (x>0, y>0):
        case (True, True):
            return 1
        case (False, True):
            return 2
        case (False, False):
            return 3
        case (True, False):
            return 4
