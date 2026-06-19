def series_sum(n):
    # Happy Coding ^_^
    output = 0.0
    for i in range(n):
        output += 1 / (1 + i*3)
    return '%.2f' % output
