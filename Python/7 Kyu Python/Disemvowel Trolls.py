def disemvowel(string_: str) -> str:
    vowels = set("aeiouAEIOU")
    return ''.join(char for char in string_ if char not in vowels)