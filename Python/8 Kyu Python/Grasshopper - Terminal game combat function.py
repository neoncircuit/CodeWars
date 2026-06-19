def combat(health, damage):
    #your code here
    while health >= 0:
        if health < damage:
            return 0
        else: 
            return health - damage  
