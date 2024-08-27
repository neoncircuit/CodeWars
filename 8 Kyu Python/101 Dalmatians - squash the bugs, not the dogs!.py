def how_many_dalmatians(n):
    dogs = ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"];
  
    match n:
        case n if n <= 10:
            return dogs[0]
        case n if n <= 50:
            return dogs[1]
        case 101:
            return dogs[3]
        case _:
            return dogs[2]
