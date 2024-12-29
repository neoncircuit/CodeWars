def next_item(xs, item):
    # TODO: Implement me
    it = iter(xs)
    for x in it:
        if x == item:
            return next(it, None)
    return None