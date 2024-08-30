def list_animals(animals):
    lst = ''
    for i, animal in enumerate(animals, start=1):
        lst += f"{i}. {animal}\n"
    return lst
