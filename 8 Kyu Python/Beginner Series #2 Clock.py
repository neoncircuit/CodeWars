def past(h: int, m: int, s: int) -> int:
    # Good Luck!
    """
    Return the time since midnight in milliseconds.
    
    
    Args:
        - h: int - Hour of the day
        - m: int - Minute of the day
        - s: int - Second of the day

    Returns:
        Time in milliseconds since midnight.
        Hour is 3.6e+6ms
        Minute is 60000ms
        Second is 1000ms
    """
    hour = (3.6e+6)*h
    min = 60000*m
    sec = 1000*s
    return hour + min + sec