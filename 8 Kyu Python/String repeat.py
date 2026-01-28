def repeat_str(repeat: int, string: str) -> str:
    """
    Given a non-negative integer n and a string s as parameters,
    return a string of s exactly n times.
    
    Args:
        - repeat: int - The number of times you want to duplicate the string
        - string: str - The string you want to duplicate
        
    Returns:
        - The duplicated string.
    """
    return "".join(string*repeat)