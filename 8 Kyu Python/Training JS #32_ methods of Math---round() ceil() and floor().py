import math

def round_it(n):
    int_part, dec_part = str(n).split('.')
    int_len = len(int_part)  
    dec_len = len(dec_part)
    return math.floor(n) if (int_len > dec_len) else math.ceil(n) if (int_len < dec_len) else round(n)