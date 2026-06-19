def other_angle(a: int, b: int) -> int:
    """
    Given 2 interior angles of a triangle, return the 3rd.
    
    Args:
        - a: int - Angle a of the triangle
        - b: int - Angle b of the triangle
        
    Returns:
        180 - a - b because all 3 angles of a triangle add up to 180 degrees.
    """
    return 180 - a - b