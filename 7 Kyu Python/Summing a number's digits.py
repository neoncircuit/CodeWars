def sum_digits(number: int) -> int:
    abs_number: int = abs(number)
    str_number: str = str(abs_number)
    digit_sum: int = 0
    
    for digit in str_number:
        digit_sum += int(digit)
        
    return digit_sum