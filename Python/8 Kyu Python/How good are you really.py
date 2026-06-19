from statistics import mean

def better_than_average(class_points, your_points):
    classAvg = mean(class_points)
    if your_points > classAvg:
        return True
    else:
        return False
