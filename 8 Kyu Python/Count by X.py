def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    sorted = []
    for i in range(1, n+1):
        sorted.append(x*i)
    return sorted
