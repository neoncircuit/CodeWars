def fillable(stock, merch, n):
    # Your code goes here.
    if merch in stock and stock[merch] >= n:
        return True
    else:
        return False
