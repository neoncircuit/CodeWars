def rot13(message):
    result = []
    
    for char in message:
        if 'a' <= char <= 'z':  
            result.append(chr((ord(char) - ord('a') + 13) % 26 + ord('a')))
        elif 'A' <= char <= 'Z':  
            result.append(chr((ord(char) - ord('A') + 13) % 26 + ord('A')))
        else:
            result.append(char)  
    
    return "".join(result)