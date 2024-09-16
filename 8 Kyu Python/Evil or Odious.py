from collections import Counter

def evil(n):
    ones = Counter(bin(n)[2:])['1']
    if ones % 2 == 0:
        return "It's Evil!"
    else: 
        return "It's Odious!"
