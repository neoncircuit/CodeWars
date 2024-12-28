def sc(n: int) -> str:
    """Given n, returns a string which fulfills with the Kata task.
    """
    return "" if n <= 1 else f"{'Aa~ '*(n-1)}Pa! Aa!" if n < 7 else f"{'Aa~ '*(n-1)}Pa!"