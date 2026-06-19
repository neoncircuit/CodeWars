def crap(garden: list[list[str]], bags: int, cap: int) -> str:
    #your code here
    for row in garden:
        if "D" in row:
            return "Dog!!"
        
    crap_count = sum(row.count("@") for row in garden)
        
    return "Cr@p" if (crap_count > (bags*cap)) else "Clean"