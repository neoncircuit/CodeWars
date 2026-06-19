# Fuel Calculator: Total Cost

In this kata you will have to write a function that takes litres and price_per_litre (in dollar) as arguments.

Purchases of 2 or more litres get a discount of 5 cents per litre, purchases of 4 or more litres get a discount of 10 cents per litre, and so on every two litres, up to a maximum discount of 25 cents per litre. But total discount per litre cannot be more than 25 cents. Return the total cost rounded to 2 decimal places. Also you can guess that there will not be negative or non-numeric inputs.

Good Luck!

## Note

1 Dollar = 100 Cents

# Given Code

```{python}
def fuel_price(litres, price_per_litre):
    pass
```

# My Solution

```{python}
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
```
