def split_and_merge(string_, separator):
    words = string_.split(" ")  # Split the input string into a list of words
    
    merged_words = []  # Create an empty list to store modified words
    
    for word in words:
        merged_word = separator.join(word)  # Join characters of each word using the separator
        merged_words.append(merged_word)  # Add the modified word to the list
    
    merged_string = " ".join(merged_words)  # Join the modified words back into a single string using space as separator
    
    return merged_string
