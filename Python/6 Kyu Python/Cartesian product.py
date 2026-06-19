def cart_prod(*sets):
    """
    Return the Cartesian product of input iterables as a set of tuples.

    Args:
        *sets: One or more iterables whose Cartesian product will be computed.

    Returns:
        A set of tuples representing the Cartesian product.
    """
    if not sets:
        return {()}
    result = {()}
    for s in sets:
        result = {r + (x,) for r in result for x in s}
    return result