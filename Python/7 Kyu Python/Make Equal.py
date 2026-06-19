def count(a: list[int], t: int, x: int) -> int:
    if x == 0:
        return sum(1 for num in a if num == t)
    
    res = 0
    for num in a:
        if abs(t - num) % x == 0:
            res += 1
    return res