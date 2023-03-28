def duplicate_count(text):
    # Your code goes here
    
    # Empty Dictionary to store count of each character in input string
    charDict = {} 
    
    # Looping through each character in input string and converts it into lowercase
    for i in text.lower():
        
        # Check if char is alphanumeric
        if i.isalnum(): 
            
            # Checks if its already in charDict
            if i in charDict:
                charDict[i] += 1 # Increments its count by 1
            else:
                charDict[i] = 1 # Adds to charDict with a count of 1
    
    count = 0
    
    # Loops through the keys of charDict and counts number of keys that have a count greater than 1
    for j in charDict:
        if charDict[j] > 1:
            count += 1

    return count
