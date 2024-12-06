def array_madness(a,b):
    # Ready, get, set, GO!!!
    sumA = sum(i ** 2 for i in a)
    sumB = sum(j ** 3 for j in b)
    return True if sumA > sumB else False