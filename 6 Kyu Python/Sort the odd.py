def sort_array(source_array):
    # Create two empty lists for odd and even numbers
    odd_nums = []
    even_nums = []

    # Iterate through the source array and add odd and even numbers to their respective lists
    for i in source_array:
        if i % 2 != 0:
            odd_nums.append(i)
        else:
            even_nums.append(i)

    # Sort the odd numbers list in ascending order
    odd_nums.sort()

    # Create a new list by iterating through the source array and replacing odd numbers with the next number in the sorted odd_nums list
    sorted_array = []
    for num in source_array:
        if num % 2 != 0:
            sorted_array.append(odd_nums.pop(0))
        else:
            sorted_array.append(num)

    return sorted_array
