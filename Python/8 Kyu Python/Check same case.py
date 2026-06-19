def same_case(a, b): 
    # your code here
    if a.isalpha() and b.isalpha():
        if (a.isupper() and b.isupper()) or (a.islower() and b.islower()):
            return 1
        else:
            return 0
    else:
        return -1