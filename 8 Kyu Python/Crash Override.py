def alias_gen(f_name, l_name):
    if not (f_name[0].isalpha() and l_name[0].isalpha()):
        return "Your name must start with a letter from A - Z."
    
    first_initial = f_name[0].upper()
    last_initial = l_name[0].upper()
    
    first_alias = FIRST_NAME.get(first_initial)
    last_alias = SURNAME.get(last_initial)
    
    return f"{first_alias} {last_alias}"