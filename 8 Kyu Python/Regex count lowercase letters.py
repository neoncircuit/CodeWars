def lowercase_count(strng):
    # Your code here
    x = 0
    for i in strng:
        if(i.islower()):
            x += 1
    return x
