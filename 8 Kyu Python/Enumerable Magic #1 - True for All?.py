def _all(seq, fun): 
    # your code here
    for i in seq:
        if not fun(i):
            return False
    return True
