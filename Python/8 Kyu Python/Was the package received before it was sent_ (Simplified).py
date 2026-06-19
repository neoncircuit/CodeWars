def was_package_received_yesterday(tz_from, tz_to, start, duration) -> bool:    
    utc_start = start - tz_from # Convert start time to UTC    
    utc_arrival = utc_start + duration # Calculate arrival time in UTC   
    destination_time = utc_arrival + tz_to # Convert UTC arrival to destination local time
    return destination_time < 0 # Determine if the package arrived the day before
