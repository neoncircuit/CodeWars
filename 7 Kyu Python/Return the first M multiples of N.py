def multiples(m: int, n: int | float) -> list[int] | list[float]:
    # Implement me! :)
    res = []
    idx = 1
    for i in range(0, m, 1):
        res.append(idx*n)
        idx += 1
    return res