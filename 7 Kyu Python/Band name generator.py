def band_name_generator(name: str) -> str:
    if name[0] == name[-1]:
        return f"{name.capitalize()}{name[1:]}"
    else:
        return f"The {name.capitalize()}"