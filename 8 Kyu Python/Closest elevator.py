def elevator(left, right, call):
    # Code on! :)
    return "left" if abs(left - call) < abs(right - call) else "right"