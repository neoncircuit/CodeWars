def remainder(a: int, b: int) -> int:
    #your code here
    smaller = min(a, b)
    larger = max(a, b)

    if smaller == 0:
        return None

    return larger % smaller