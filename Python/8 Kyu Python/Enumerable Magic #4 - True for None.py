def none(lst: list[int], func) -> bool:
    """
    Return True if no element in the list satisfies the predicate.

    Check whether the predicate function `func` returns False for every element
    in `lst`. If the list is empty, returns True.

    Args:
        - lst: list[int]: A list of integers to test.
        - func: callable: A predicate that accepts an int and returns a bool.
                          If func(x) is True for any element x, this function
                          returns False. Remember to import typing when using this.

    Returns:
        bool: True if `func` returns False for all elements in `lst` (or if
              `lst` is empty). Returns False if `func` returns True for at
              least one element.

    Examples:
        >>> none([0, 1, 2], lambda x: x > 100)
        True
        >>> none([], lambda x: x == 0)
        True
        >>> none([1, 2, 3], lambda x: x % 2 == 0)
        False
    """
    for x in lst:
        if func(x):
            return False
    return True