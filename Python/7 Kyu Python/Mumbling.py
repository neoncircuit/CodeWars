def accum(st):
    return "-".join(char.upper() + char().lower()*i for i, char in enumerate(st))