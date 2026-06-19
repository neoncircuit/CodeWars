def tower_builder(n_floors):
    # build here
    res = []
    width = n_floors*2 - 1
    for i in range(n_floors):
        numBlocks = i*2 + 1
        spaces = " " * ((width-numBlocks) // 2)
        blocks = "*" * numBlocks
        row = spaces + blocks + spaces
        res.append(row)
    return res
