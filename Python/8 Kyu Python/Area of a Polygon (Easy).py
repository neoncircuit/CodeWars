def polygon_area(a: int, b: int, c: int, d: int) -> int:
    rect: int = b * c
    tri1: int = 0.5 * (c-a) * d
    tri2: int = 0.5 * (c-a) * d
    return rect - tri1 - tri2