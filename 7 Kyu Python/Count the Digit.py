def nb_dig(n, d):
    # Generate squares of numbers from 0 to n
    squares = [str(i ** 2) for i in range(n + 1)]
    
    # Count occurrences of digit d in all squares
    total_count = sum(square.count(str(d)) for square in squares)
    
    return total_count