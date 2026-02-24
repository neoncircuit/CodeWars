def case_id(c_str: str) -> str:
    # your code here
    if "-" in c_str:
        if "_" in c_str or "--" in c_str or any(c.isupper() for c in c_str): 
            return "none" 
        return "kebab"
        
    if "_" in c_str:
        if "-" in c_str or "__" in c_str or any(c.isupper() for c in c_str):
            return "none" 
        return "snake" 
        
    if "-" not in c_str and "_" not in c_str:
        if c_str.lower() == c_str:
            return "none"
        if not c_str[0].islower():
            return "none"
        if any(c == "_" or c == "-" for c in c_str):
            return "none"
        return "camel"
    
    return "none"