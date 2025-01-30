def gimme(input_array):
    # Implement this function
    sorted_array = sorted(input_array)
    middle_value = sorted_array[1]  
    return input_array.index(middle_value)