def to_alternating_case(string):
    return ''.join([letter.lower() if letter.isupper() else letter.upper() for letter in string])