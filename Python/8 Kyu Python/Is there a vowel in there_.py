def is_vow(inp):
    vowels = {97: 'a', 101: 'e', 105: 'i', 111: 'o', 117: 'u'}
    result = []
    for num in inp:
        if num in vowels:
            result.append(vowels[num])
        else:
            result.append(num)  
    return result