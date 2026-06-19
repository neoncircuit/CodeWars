from typing import List

def how_much_coffee(events: List[str]) -> int | str:
    res = 0
    substringL, substringU = "other", "OTHER"
    for event in events:
        if substringL in event or substringU in event:
            continue
        elif event.islower():
            res += 1
        elif event.isupper():
            res += 2
    return "You need extra sleep" if res > 3 else res