def sale_hotdogs(n):
    # your code here
    match n:
        case _ if 5 <= n < 10:
            return n*95
        case _ if n >= 10:
            return n*90
        case _:
            return n*100