def change_me(input_money):
    # your code here
    accepted = {
        "£5": 500,
        "£2": 200,
        "£1": 100,
        "50p": 50,
        "20p": 20
    }

    change_denominations = {
        "20p": 20,
        "10p": 10
    }

    if input_money not in accepted:
        return input_money  

    value = accepted[input_money]

    change = []
    
    for denomination, denom_value in change_denominations.items():
        while value >= denom_value:
            change.append(denomination)
            value -= denom_value

    if input_money == "20p":
        change = ["10p", "10p"]
    
    return " ".join(change)
