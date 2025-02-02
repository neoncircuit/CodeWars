def mxdiflg(a1, a2):
    # your code
    if not a1 or not a2:
        return -1
    
    length_a1 = [len(s) for s in a1]
    length_a2 = [len(s) for s in a2]
    
    max_a1 = max(length_a1)
    min_a1 = min(length_a1)
    max_a2 = max(length_a2)
    min_a2 = min(length_a2)
    
    return max(max_a1 - min_a2, max_a2 - min_a1)