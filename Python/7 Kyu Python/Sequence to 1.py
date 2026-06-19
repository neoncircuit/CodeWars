def seq_to_one(n: int) -> list[int]:
    int_min, int_max = -9999, 9999
    while n >= int_min and n <= int_max:
        return list(range(n, 0, -1)) if n >= 1 else list(range(n, 2, 1))