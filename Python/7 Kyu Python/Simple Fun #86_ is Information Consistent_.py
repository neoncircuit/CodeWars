def is_information_consistent(evidences) -> bool:
    # Transpose the matrix to check testimonies defendant-wise
    for j in range(len(evidences[0])):  # Iterate over defendants (columns)
        testimonies = [evidences[i][j] for i in range(len(evidences))]
        if 1 in testimonies and -1 in testimonies:  # Check for conflict
            return False
    return True  