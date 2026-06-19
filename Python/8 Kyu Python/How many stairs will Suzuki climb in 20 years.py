def stairs_in_20(stairs):
    # Calculate the sum of stairs climbed in a year using a for loop
    one_year_total = 0
    for day in stairs:
        one_year_total += sum(day)
    
    # Calculate the estimate for 20 years
    twenty_year_estimate = one_year_total * 20
    
    return twenty_year_estimate
