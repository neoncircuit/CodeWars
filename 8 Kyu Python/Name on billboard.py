def billboard(name, price=30):
    bill = 0 
    for i in name:
        bill += price
    return bill
