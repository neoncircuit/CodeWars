from typing import Set, Any

def outed(meet: Set[Any], boss: str) -> str:
    # your code here!
    total = sum(meet.values()) + meet[boss]
    res = total / len(meet)
    return "Nice Work Champ!" if res > 5 else "Get Out Now!"