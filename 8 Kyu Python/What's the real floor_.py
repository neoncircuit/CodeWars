def get_real_floor(n):
    # code here
    while n != 13:
        return n if n < 0 else 0 if n < 2 else n-1 if n < 14 else n-2