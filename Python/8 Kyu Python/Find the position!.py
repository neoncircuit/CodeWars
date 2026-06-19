def position(letter):
    letter = letter.lower()
    if 'a' <= letter <= 'z':
        return f"Position of alphabet: {ord(letter) - ord('a') + 1}"
    else:
        return None