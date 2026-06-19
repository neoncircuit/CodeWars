def starting_mark(height):
    while height >= 1.22 and height <= 2.13:
        # y = mx + c
        x1, y1 = 1.52, 9.45
        x2, y2 = 1.83, 10.67
        
        # y2 - y1: Difference in height
        # x2 - x1: Difference in starting positions
        m = (y2 - y1)/(x2 - x1)
        
        c = y1 - m * x1
        
        start = m * height + c
        
        return round(start, 2)
        break
