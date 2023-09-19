def array(string):
    # Split the input string by commas and remove leading/trailing spaces
    sequences = [s.strip() for s in string.split(',')]

    # Check if there are more than two elements in the list
    if len(sequences) > 2:
        # Join the remaining elements with spaces
        return ' '.join(sequences[1:-1])
    else:
        # Return NULL if there are not enough elements
        return None
