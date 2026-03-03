import operator

def calculate(num1: float | int, operation: str, num2: float | int) -> str: 
    # your code here
    OPERATORS = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }
    func = OPERATORS.get(operation)
    
    if func is None:
        return None
    
    if operation == '/' and num2 == 0:
        return None

    try:
        return func(num1, num2)
    except ZeroDivisonError:
        return None