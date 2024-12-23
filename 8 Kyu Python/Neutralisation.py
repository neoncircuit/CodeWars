def neutralise(s1, s2):
    result = []
    for char1, char2 in zip(s1, s2):
        if char1 == char2:
            result.append(char1)
        else:
            result.append("0")
    return "".join(result)