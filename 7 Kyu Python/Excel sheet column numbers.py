def title_to_number(title: str) -> int:
    res = 0
    for char in title:
        res = res * 26 + (ord(char) - ord('A') + 1)
    return res