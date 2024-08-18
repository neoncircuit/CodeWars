def change_me(money): 
    match money:
        case "£5" : return " ".join(["20p"] * 25)
        case "£2" : return " ".join(["20p"] * 10)
        case "£1" : return " ".join(["20p"] * 5)
        case "50p": return "20p 20p 10p"
        case "20p": return "10p 10p"
        case   _  : return money
