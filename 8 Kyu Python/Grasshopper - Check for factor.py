def check_for_factor(base: int, factor: int) -> bool:
    # your code here
    """
    Check if "factor" is a factor of "base"
    
    Args:
        - base: int - Base number
        - factor: int - Number that can be multiplied with other numbers
    Returns:
        Return True if "factor" is a factor of "base". Else False
    """
    return base % factor == 0