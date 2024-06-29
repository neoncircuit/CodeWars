def symmetric_point(p, q):
    # your code here
    px, py = p
    qx, qy = q
    
    p1x = 2 * qx - px
    p1y = 2 * qy - py
    
    return [p1x, p1y]
