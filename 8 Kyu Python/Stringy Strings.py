def stringy(size):
    x = ""
    
    for i in range(size):
        if i % 2 == 0:
            x += '1'
        else:
            x += '0'
    
    return x
