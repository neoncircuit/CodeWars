from typing import Optional
from collections import Counter

def digit_signature(num: int) -> Counter[str]:
    return Counter(str(num))

def find_lowest_int(k: int, max_search: int = 1000000) -> Optional[int]:
    for n in range(1, max_search, 1):
        a = k * n
        b = (k + 1) * n
        if digit_signature(a) == digit_signature(b):
            return n
    return None