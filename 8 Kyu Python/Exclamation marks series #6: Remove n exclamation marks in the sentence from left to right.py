def remove(st, n):
    count = 0
    result = ''
    for char in st:
        if char == '!' and count < n:
            count += 1
        else:
            result += char
    return result
