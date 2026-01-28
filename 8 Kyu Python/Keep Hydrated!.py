import math

def litres(time: float) -> int:
    """
    Nathan drinks 0.5 litres of water per hour of cycling.
    
    Args:
        Number of hours as a float.
        
    Returns:
        Number of litres of water required, rounded down. 
    """
    return math.floor(time/2)