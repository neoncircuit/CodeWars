import string

def is_pangram(st):
    # Create a set of all lowercase alphabetic characters
    alphabet = set(string.ascii_lowercase)
    
    # Normalize input: lowercase and filter alphabetic characters
    s_letters = set(c.lower() for c in st if c.isalpha())
    
    # Check if the input contains all the letters in the alphabet
    return alphabet.issubset(s_letters)