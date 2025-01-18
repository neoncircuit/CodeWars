def count(s):
    # The function code should be here
    dict = {}
    
    for letter in s:
        if letter in dict:
            dict[letter] += 1
        else: 
            dict[letter] = 1
    
    return dict