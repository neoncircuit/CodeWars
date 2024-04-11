def well(x):
    #your code here
    g = x.count("good")
    if g == 1:
        return "Publish!"
    elif g == 2:
        return "Publish!"
    elif g > 2:
        return "I smell a series!"
    else:
        return "Fail!"
