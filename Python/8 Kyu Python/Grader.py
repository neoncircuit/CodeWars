def grader(score):
    match score:
        case s if 0.9 <= s <= 1:
            return "A"            
        case s if 0.8 <= s < 0.9:
            return "B"            
        case s if 0.7 <= s < 0.8:
            return "C"            
        case s if 0.6 <= s < 0.7:
            return "D"            
        case _:
            return "F"