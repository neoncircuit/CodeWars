def dig_pow(n, p):
    # your code
    
    # Convert the number to a string to iterate through its digits
    digits = [int(digit) for digit in str(n)]
    
    # Compute the sum of powers
    total_sum = sum(digit ** (p + i) for i, digit in enumerate(digits))
    
    # Check if total_sum is divisible by n
    if total_sum % n == 0:
        return total_sum // n  # Calculate and return k
    else:
        return -1  # If not divisible, return -1