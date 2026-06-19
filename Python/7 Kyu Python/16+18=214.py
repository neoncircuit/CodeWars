def add(num1: int, num2: int) -> int:
    if num1 == num2 and num1 == 0: return 0

    list_num1, list_num2 = list(str(num1)), list(str(num2))
    
    len1, len2 = len(list_num1), len(list_num2)
    
    diff = abs(len1 - len2)
    
    if len1 < len2:
        list_num1 = ['0'] * (diff) + list_num1
    elif len2 < len1:
        list_num2 = ['0'] * (diff) + list_num2
        
    summed_digits = []
    for i in range(len(list_num1)):
        sum_digit = int(list_num1[i]) + int(list_num2[i])
        summed_digits.append(str(sum_digit))
        
    return int(''.join(summed_digits))