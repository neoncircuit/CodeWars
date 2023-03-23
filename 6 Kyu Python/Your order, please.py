def order(sentence):
  # split the input string into a list of words
    words = sentence.split()
    
    # create a dictionary to store the order of each word
    order = {}
    for word in words:
        for char in word:
            if char.isdigit():
                order[word] = int(char)
    
    # sort the words based on their order
    sorted_words = sorted(words, key=lambda x: order[x])
    
    # join the sorted words back into a string
    result = ' '.join(sorted_words)
    
    return result
