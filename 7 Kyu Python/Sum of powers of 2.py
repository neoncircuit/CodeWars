# return an array of numbers (that are a power of 2)
# for which the input "n" is the sum
from typing import List

def powers(n: int) -> List[int]:
    res = []
    i = 0
    while n:
        if n & 1:
            res.append(2**i)
        n >>= 1
        i += 1
    return res