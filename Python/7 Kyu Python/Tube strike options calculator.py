def calculator(distance: int, bus_drive: int, bus_walk: int) -> str:
    # Your code here
    walk_time: float = distance / 5 
    bus_time: float = (bus_walk / 5) + (bus_drive / 8)
    
    if walk_time > 2:
        return "Bus" 
    elif (walk_time < 1/6) or (walk_time <= bus_time): 
        return "Walk"
    else:
        return "Bus"