from collections import Counter

def dominator(arr: list[int]) -> int:
    if not arr:
        return -1
    
    counts = Counter(arr)
    candidate, appearance = counts.most_common(1)[0]
    
    if appearance > len(arr) // 2:
        return candidate
    else: 
        return -1
