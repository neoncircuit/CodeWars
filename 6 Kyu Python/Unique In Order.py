def unique_in_order(sequence):
    result = []
    for i, char in enumerate(sequence):
        # Add the first character or if it's different from the previous one
        if i == 0 or char != sequence[i - 1]:
            result.append(char)
    return result