def shark(pontoon_distance, shark_distance, you_speed, shark_speed, dolphin=False):
    # Don't get eaten!
    if dolphin == True:
        shark_speed /= 2      
    return "Alive!" if pontoon_distance/you_speed < shark_distance/shark_speed else "Shark Bait!"