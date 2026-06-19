# speed of aircrafts is given in *knots*
# travelTime is in *minutes*
# travel distance should be returned in *kilometers*

def travel_distance(avg_speed: int, travel_time: int) -> float:
    """
    Calculates flight distance in Kilometers based on speed in Knots 
    and time in Minutes.
    
    Distance traveled = avg_speed * travel_hours * KM_PER_NAUT_MILE
    
    args:
        avg_speed: int
        travel_time: int
    returns:
        travel_kms: float
    """
    # 1 Nautical Mile = 1.852 Kilometers
    KM_PER_NAUT_MILE = 1.852 
    travel_hours = travel_time / 60
    travel_miles = avg_speed * travel_hours
    travel_kms = travel_miles * KM_PER_NAUT_MILE
    return round(travel_kms, 1)