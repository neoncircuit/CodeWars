from typing import List

def breach_attempts(hackers: List[int], security_level: int, increase: int) -> int:
    if not hackers:
        return 0
    
    breaches = 0
    for attempt in hackers:
        if attempt > security_level:
            breaches += 1
        else:
            security_level += increase
    return breaches