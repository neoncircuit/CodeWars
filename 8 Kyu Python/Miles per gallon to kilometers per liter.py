def converter(mpg):
    # 1 Imperial Gallon = 4.54609188 litres
    # 1 Mile = 1.609344 kilometres
    x = 1.609344 / 4.54609188
    kpl = mpg * x
    return round(kpl, 2)  # Round the result to two decimal points
