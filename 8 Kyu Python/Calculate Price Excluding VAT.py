def excluding_vat_price(price):
    if price is None:
        return -1
    else:
        finalPrice = price / 1.15
        return round(finalPrice, 2)
