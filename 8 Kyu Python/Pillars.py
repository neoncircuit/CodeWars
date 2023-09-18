def pillars(num_pill, dist, width):
    if num_pill < 1:
        return 0
    elif num_pill == 1:
        return 0
    elif dist < 10 or dist > 30:
        return 0
    elif width < 10 or width > 50:
        return 0
    else:
        return (num_pill - 1) * dist * 100 + (num_pill - 2) * width
