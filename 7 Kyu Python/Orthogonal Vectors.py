def is_orthogonal(u: list[int], v: list[int]) -> bool: 
    # your code here
    return sum(a*b for a, b in zip(u, v)) == 0