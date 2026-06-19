def area_or_perimeter(l: int , w: int) -> int:
    # return your answer
    """
    Given a 4 sided polygon, return area if it is a square, otherwise perimeter if rectangle
    
    Args:
        l: int - Length of the polygon
        w: int - Width of the polygon
        
    Returns:
        Area of the polygon if it is a square.
        Perimeter of the polygon if it is a rectangle
    """
    return l*w if (l == w) else (l+w)*2