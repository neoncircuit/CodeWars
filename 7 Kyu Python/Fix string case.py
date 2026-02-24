def solve(s: str) -> str:
    upper_count, lower_count = 0, 0
    for c in s:
        if c.isupper():
            upper_count += 1
        else:
            lower_count += 1
    
    return s.upper() if (upper_count > lower_count) else s.lower()