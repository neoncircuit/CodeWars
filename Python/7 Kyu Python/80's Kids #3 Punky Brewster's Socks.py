from typing import List
from collections import Counter

def get_socks(name: str, socks: List[str]) -> List[str]:
    #your code here
    counts = Counter(socks)
    
    if name == "Henry":
        for color, count in counts.items():
            if count >= 2:
                return [color, color]
        return []
    else:
        unique_colors = list(counts.keys())
        return unique_colors[:2] if (len(unique_colors) >= 2) else []