def two_sort(array):
    array.sort() # Alphabetical sort
    
    x = array[0] # First string from sorted array
    
    y = '***'.join(x) # Use '***' to seperate each character in First String
    
    return y
