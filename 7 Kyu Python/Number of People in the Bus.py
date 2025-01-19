def number(bus_stops):
    # Good Luck!
    remaining_people = 0
    
    for board, alight in bus_stops:
        remaining_people += board
        remaining_people -= alight
    
    return remaining_people