def beasts(heads, tails):
    # [orthus, hydra]
    # heads = 2o + 5h
    # tails = o + h
    if (heads - 2 * tails) % 3 != 0 or (heads - 2 * tails) < 0:
        return "No solutions"
    
    H = (heads - 2 * tails) // 3
    O = tails - H
    
    if O < 0 or H < 0:
        return "No solutions"
    
    return [O, H]