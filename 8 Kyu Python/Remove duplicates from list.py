def distinct(seq):
    x = []
    for i in seq:
        if i not in x:
            x.append(i)
    return x
