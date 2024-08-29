def logical_calc(array, op):
    match op:
        case "AND":
            return all(array)
        case "OR":
            return any(array)
        case "XOR":
            res = array[0]
            for i in array[1:]:
                res  ^= i
            return res
