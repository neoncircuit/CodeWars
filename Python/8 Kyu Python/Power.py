def number_to_pwr(number, p): 
    # your code here
    result = 1 
    for _ in range(p):  
        result *= number  
    return result