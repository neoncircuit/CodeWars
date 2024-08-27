from math import ceil

def calculate_tip(amount, rating):
    rating = rating.lower()
    
    #your code here
    match rating:
        case "terrible":
            return 0
        case "poor":
            return ceil(5/100 * amount)
        case "good":
            return ceil(10/100 * amount)
        case "great":
            return ceil(15/100 * amount)
        case "excellent":
            return ceil(20/100 * amount)
        case _:
            return "Rating not recognised"
