def basic_op(operator, value1, value2):
    #your code here
    match operator:
        case "+":
            out = value1 + value2
        case "-":
            out = value1 - value2
        case "*":
            out = value1 * value2
        case "/":
            out = value1 / value2
    return out
