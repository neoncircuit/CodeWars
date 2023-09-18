def flick_switch(lst):
    x = []
    y = True
    
    for i in lst:
        if i == "flick":
            y = not y
        x.append(y)
    
    return x
