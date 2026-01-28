def goals(laLiga: int, copaDelRey: int, championsLeague: int) -> int:
    """
    Return the total number of Messi's goals in all 3 leagues.
    
    Args:
        - laLiga: int - Number of Messi goals scored in the LaLiga league
        - copaDelRey: int - Number of Messi goals scored in the Copa del Rey league
        - championsLeague: int - Number of Messi goals scored in the Champions league
    
    Returns:
        Total number of goals that Messi scored
    """
    return sum([laLiga, copaDelRey, championsLeague])