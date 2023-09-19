import math

def duty_free(price, discount, holiday_cost):
    discountedPrice = price * (discount/100)
    noOfBottles = math.floor(holiday_cost/discountedPrice)
    return noOfBottles
