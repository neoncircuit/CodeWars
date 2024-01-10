def calculate_age(year_of_birth, current_year):
    x = abs(current_year - year_of_birth)
    if current_year < year_of_birth:
        if x == 1:
            return f"You will be born in {x} year."
        else:
            return f"You will be born in {x} years."
    elif current_year > year_of_birth:
        if x == 1:
            return f"You are {x} year old."
        else:
            return f"You are {x} years old."
    else:
        return "You were born this very year!"
