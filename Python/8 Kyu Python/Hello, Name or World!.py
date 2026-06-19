def hello(name=""):
    match name:
        case "" | None:
            return "Hello, World!"
        case _:
            capitalized_name = name.capitalize()
            return f"Hello, {capitalized_name}!"