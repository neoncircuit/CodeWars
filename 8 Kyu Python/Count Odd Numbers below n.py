def odd_count(n):
    odd = []
    for i in range(n):
        if i % 2 != 0:
            odd.append(i)
    return len(odd)
