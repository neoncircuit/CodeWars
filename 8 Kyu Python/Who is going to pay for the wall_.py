def who_is_paying(name) -> list:
    #your code here
    return [name] if len(name) <= 2 else [name, name[:2]]