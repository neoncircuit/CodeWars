def expanded_form(num):
    mult = 10
    res = []
    while num > 1:
        rem = num % mult
        if rem > 0:
            # Add as index 0 of res. Equivalent of res.unshift(rem) in JS
            res.insert(0, rem) 
        num -= rem
        mult *= 10
    # Convert each int in res to a string using the map and str function
    return " + ".join(map(str, res))
