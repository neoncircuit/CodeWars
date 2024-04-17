def maps(a):
    def double(n):
        return n*2
    
    return list(map(double, a))
