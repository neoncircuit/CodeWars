def correct(s):
    if "5" in s:
        s = s.replace("5", "S")
    if "0" in s:
        s = s.replace("0", "O")
    if "1" in s:
        s = s.replace("1", "I")
    return s
