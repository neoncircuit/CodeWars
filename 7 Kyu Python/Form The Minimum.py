def min_value(digits):
    # your code here
    unique_digits = set(digits) # Remove duplicates by converting to a set
    sorted_digits = sorted(unique_digits) # Sort the unique digits
    return int("".join(map(str, sorted_digits))) # Join the digits into a string and convert to an integer