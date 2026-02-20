from typing import Tuple

def solution(first: int, second: int) -> Tuple[int, int]:
    if first == second and first == 0:
        return (0, 0)
    
    while True:
        prev = second - first
        
        if prev == 0:
            return (0, first)
        
        if prev > first: 
            return (first, second)
        
        second, first = first, prev