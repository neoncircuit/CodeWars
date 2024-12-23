def subtract_sum(number):    
    #fruit name like "apple"
    if not (10 <= number < 10000):
        raise ValueError("Input must be between 10 and 9999.")
    
    fruits = {
        1: "kiwi", 2: "pear", 3: "kiwi", 4: "banana", 5: "melon",
        6: "banana", 7: "melon", 8: "pineapple", 9: "apple", 10: "apple",
        11: "kiwi", 12: "banana", 13: "kiwi", 14: "banana", 15: "melon",
        16: "pineapple", 17: "apple", 18: "apple", 19: "kiwi", 20: "pear",
        21: "kiwi", 22: "banana", 23: "kiwi", 24: "apple", 25: "melon",
        26: "banana", 27: "melon", 28: "pineapple", 29: "apple", 30: "apple",
        31: "kiwi", 32: "banana", 33: "kiwi", 34: "banana", 35: "melon",
        36: "banana", 37: "melon", 38: "pineapple", 39: "apple", 40: "pear",
        41: "kiwi", 42: "banana", 43: "kiwi", 44: "apple", 45: "apple",
        46: "banana", 47: "melon", 48: "pineapple", 49: "apple", 50: "apple",
        51: "kiwi", 52: "banana", 53: "kiwi", 54: "apple", 55: "melon",
        56: "banana", 57: "melon", 58: "pineapple", 59: "apple", 60: "apple",
        61: "kiwi", 62: "banana", 63: "kiwi", 64: "banana", 65: "melon",
        66: "banana", 67: "melon", 68: "pineapple", 69: "apple", 70: "apple",
        71: "kiwi", 72: "banana", 73: "kiwi", 74: "banana", 75: "melon",
        76: "pineapple", 77: "apple", 78: "apple", 79: "kiwi", 80: "banana",
        81: "apple", 82: "melon", 83: "pineapple", 84: "apple", 85: "kiwi",
        86: "banana", 87: "melon", 88: "pineapple", 89: "apple", 90: "apple",
        91: "kiwi", 92: "banana", 93: "kiwi", 94: "banana", 95: "melon",
        96: "banana", 97: "melon", 98: "pineapple", 99: "apple", 100: "apple"
    }

    while number not in fruits:
        digit_sum = sum(int(digit) for digit in str(number))
        number -= digit_sum

    return fruits[number]