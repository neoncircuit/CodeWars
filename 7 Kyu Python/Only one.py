def only_one(*bools: bool) -> bool:
    true_count = sum(1 for item in bools if item is True)
    return true_count == 1