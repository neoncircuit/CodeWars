def get_middle(s: str) -> str:
    if len(s) == 1 or s == "":
        return s
    
    mid = len(s) // 2
    if len(s) % 2 == 0:
        return s[mid-1:mid+1]
    else:
        return s[mid]