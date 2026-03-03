def fly_by(lamps: str, drone: str) -> str:
    #hack the lamps
    n = min(len(drone), len(lamps))
    return 'o'*n + lamps[n:]