def trouble(x: list[int], t: int) -> list[int]:
    idx = 0
    while idx < len(x) - 1:
        if x[idx] + x[idx+1] == t:
            x.pop(idx+1)
        else:
            idx += 1
    return x