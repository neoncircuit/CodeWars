def find_nb(m):
    vol = 0
    n = 0
    while vol < m:
        n += 1
        vol += pow(n, 3)
    if vol == m:
        return n
    else: 
        return -1
