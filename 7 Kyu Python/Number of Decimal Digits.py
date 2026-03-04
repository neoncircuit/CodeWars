def digits(n: float) -> int:
    # your code here
    s = str(abs(n))
    return s.index('.') if '.' in s else len(s)