def rental_car_cost(d):
    # your code
    rent = d * 40
    if d >= 7:
        rent -= 50
    elif d >= 3:
        rent -= 20
    return rent
