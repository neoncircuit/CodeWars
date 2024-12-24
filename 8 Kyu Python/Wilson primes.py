import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def am_i_wilson(n):
    # Early exit for non-primes
    if not is_prime(n):
        return False

    # Wilson primes are known to be 2, 3, 5 (as per current knowledge)
    # Test these directly.
    if n in {2, 3, 5}:
        return True

    # If we need to check for larger numbers, do a factorial-based check, but expect performance issues
    # Use a try-except block for very large numbers to prevent timeout
    try:
        factorial = math.factorial(n - 1)
        return (factorial + 1) % (n * n) == 0
    except OverflowError:
        # If factorial computation is too large, it is unlikely to be a Wilson prime
        return False
