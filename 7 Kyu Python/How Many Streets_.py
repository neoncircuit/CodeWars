def count_streets(streets, drivers):
    # Create a dictionary for street indices
    street_indices = {street: index for index, street in enumerate(streets)}
    
    # Calculate the number of streets crossed for each driver
    result = []
    for entry, exit in drivers:
        entry_index = street_indices[entry]
        exit_index = street_indices[exit]
        # Absolute difference minus 1 gives the number of streets crossed
        result.append(abs(exit_index - entry_index) - 1)
    
    return result