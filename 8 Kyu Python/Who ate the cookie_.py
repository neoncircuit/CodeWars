def cookie(x) -> str:
    #Good Luck
    if isinstance(x, str):
        name = "Zach"
    elif isinstance(x, (int, float)) and not isinstance(x, bool):
        name = "Monica"
    else:
        name = "the dog"
    return f"Who ate the last cookie? It was {name}!"