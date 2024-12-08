def nba_extrap(ppg, mpg):
    return 0 if ppg == mpg == 0 else round((48/mpg)*ppg, 1)