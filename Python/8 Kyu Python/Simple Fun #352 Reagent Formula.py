def isValid(formula):
    materials = set(formula)
    
    if 1 in materials and 2 in materials:
        return False
    if 3 in materials and 4 in materials:
        return False
    if 5 in materials and 6 not in materials:
        return False
    if 6 in materials and 5 not in materials:
        return False
    if 7 not in materials and 8 not in materials:
        return False
    
    return True
