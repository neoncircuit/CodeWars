def men_from_boys(arr: list[int]) -> list[int]:
    #your code here
    if not isinstance(arr, list):
        raise TypeError("Input must be a list.")
    
    unique_numbers = set(arr)  # Remove duplicates
    evens = sorted([x for x in unique_numbers if x % 2 == 0])
    odds = sorted([x for x in unique_numbers if x % 2 != 0], reverse=True)
    return evens + odds