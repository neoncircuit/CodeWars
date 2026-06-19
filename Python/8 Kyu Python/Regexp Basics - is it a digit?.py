import re

def is_digit(n):
    #your code here
    if re.fullmatch(r"[0-9]", n) and 0 <= int(n) < 10:
        return True
    else:
        return False