def is_opposite(s1,s2):
    pass # your code here
    if s1 == "" or s2 == "":
        return False
    elif s2 == s1.swapcase():
        return True
    else:
        return False
