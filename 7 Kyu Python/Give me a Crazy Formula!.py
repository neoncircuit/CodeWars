def crazy_formula(n: int) -> int:
    while len(str(n)) > 1:
        print(f"Processing number: {n}")
        digits = list(map(int, str(n)))

        if len(digits) % 2 == 0:
            # If the number of digits is even, remove the last digit
            digits.pop()
        
        if len(digits) > 1:
            # Get middle and last digits
            mid_index = len(digits) // 2
            mid_digit = digits[mid_index]
            last_digit = digits[-1]

            if mid_digit % 2 == 1:
                # a. If the middle digit is odd, subtract it instead of adding
                digits[mid_index] = -mid_digit
            elif mid_digit % 2 == 0 and last_digit % 2 == 0:
                # b. If both the middle digit and the last digit are even, subtract the last digit instead of adding
                digits[-1] = -last_digit
            elif mid_digit % 2 == 0 and last_digit % 2 == 1:
                # c. If the middle digit is even but the last digit is odd, the first digit must be squared
                digits[0] **= 2

        # Calculate the updated number and ensure it is non-negative
        n = abs(sum(digits))
        print(f"Updated number: {n}")

    return n
