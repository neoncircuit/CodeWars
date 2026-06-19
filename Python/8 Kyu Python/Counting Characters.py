def count_char_occurrences(string_input: str, char_input: chr) -> int:
    """
    Given an input string and char 
    Find the number of occurrences of the char input inside the string input
    
    args:
        string_input: str
        char_input: chr
    
    returns:
        int
    """
    return string_input.count(char_input)