def mouth_size(animal): 
    animal2 = animal.lower()
    # code here
    match animal2:
        case "alligator":
            return "small"
        case _:
            return "wide"