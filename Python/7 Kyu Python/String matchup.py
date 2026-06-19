from typing import List
from collections import Counter

def solve(a: List[str], b: List[str]) -> List[int]:
    freq = Counter(a) 
    return [freq[x] for x in b]