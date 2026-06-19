def calculator(x,y,op):
    while type(x) == int and type(y) == int and type(op) == str and op in {"+", "-", "/", "*"}:
        return eval(f"{x} {op} {y}")
        break
    return "unknown value"