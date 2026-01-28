def simple_multiplication(number: int) -> int:
    # Your code goes here
    """
    Multiply a number by 8 if even. Else multiply by 9
    
    Args:
        number: int - Input number
        
    Returns:
        number*8 if even 
        number*9 if odd
    """
    return number*8 if (number%2 == 0) else number*9