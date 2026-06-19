import math

def quarter_of(month: int) -> int:
    # your code here
    """
    Given a month as an integer from 1 to 12, 
    return to which quarter of the year it belongs as an integer number.
    
    Args:
        month: int - The month as an integer
    
    Returns:
        The quarter of the year as an integer. Eg. 3rd quarter returns 3
    """
    return math.ceil(month/3)