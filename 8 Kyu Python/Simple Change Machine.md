# Simple Change Machine

Your task is to create a change machine.

The machine accepts a single coins or notes, and returns change in 20p and 10p coins. The machine will try to avoid returning its exact input, but will otherwise return as few coins as possible. For example, a 50p piece should become two 20p pieces and one 10p piece, but a 20p piece should become two 10p pieces.

The machine can exclusively process these coins and notes: £5, £2, £1, 50p, 20p. Any coins and notes which are not accepted by the machine will be returned unprocessed. For example, if you were to put a £20 note into the machine, it would be returned to you and not broken into change. (Note that £1 is worth 100p.)

This change machine is programmed to accept and distribute strings rather than numbers. The input will be a string containing the coin or note to be processed, and the change should be returned as one string with the coin names separated by single spaces with no commas. The values of the string should be in descending order. For example, an input of "50p" should yield the exact string "20p 20p 10p".

# Given Code

```{python}
def change_me(money): 
    # your code here
    pass
```

# My Solution

```{python}
def change_me(money): 
    match money:
        case "£5" : return " ".join(["20p"] * 25)
        case "£2" : return " ".join(["20p"] * 10)
        case "£1" : return " ".join(["20p"] * 5)
        case "50p": return "20p 20p 10p"
        case "20p": return "10p 10p"
        case   _  : return money
```

# My Solution 2
```{python}
def change_me(input_money):
    # Define accepted denominations and their values in pence
    accepted = {
        "£5": 500,
        "£2": 200,
        "£1": 100,
        "50p": 50,
        "20p": 20
    }

    # Define the output denominations in pence
    change_denominations = {
        "20p": 20,
        "10p": 10
    }

    # Check if the input money is accepted
    if input_money not in accepted:
        return input_money  # Return unprocessed if not accepted

    # Get the value in pence
    value = accepted[input_money]

    # Generate the change
    change = []
    
    # Always prefer 20p coins, then use 10p coins
    for denomination, denom_value in change_denominations.items():
        while value >= denom_value:
            change.append(denomination)
            value -= denom_value

    # If the input was exactly a 20p coin, avoid returning the same
    if input_money == "20p":
        change = ["10p", "10p"]
    
    # Join the change list into a string
    return " ".join(change)
```
