def flip(d, a):
    # Do some magic
    if d == 'L':
        a.sort(reverse=True)
    elif d == 'R':
        a.sort()
    
    return a
