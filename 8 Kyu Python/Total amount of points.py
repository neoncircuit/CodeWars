def points(games):
    points = 0
    for game in games:
        x, y = map(int, game.split(':'))  
        if x > y:
            points += 3  
        elif x < y:
            points += 0  
        else:
            points += 1  
    return points
