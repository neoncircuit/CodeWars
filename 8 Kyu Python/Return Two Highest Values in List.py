# Create a set of distinct values from the input list arg1
    distinct_values = set(arg1)

    # Sort the distinct values in descending order
    sorted_values = sorted(distinct_values, reverse=True)

    # Check if there are at least two distinct values
    if len(sorted_values) >= 2:
        # Return the first two values if there are at least two
        return sorted_values[:2]
    elif len(sorted_values) == 1:
        # If there is only one distinct value, return it
        return [sorted_values[0]]
    else:
        # If there are no distinct values, return an empty list
        return []
