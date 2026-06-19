def fuel_price(litres, price_per_litre):
    match litres:
        case litres if litres >= 10:
            discount = 0.25
        case litres if litres >= 8:
            discount = 0.2
        case litres if litres >= 6:
            discount = 0.15
        case litres if litres >= 4:
            discount = 0.1
        case litres if litres >= 2:
            discount = 0.05
        case _:
            discount = 0
    
    price = litres * (price_per_litre - discount)
    
    return round(price, 2)
