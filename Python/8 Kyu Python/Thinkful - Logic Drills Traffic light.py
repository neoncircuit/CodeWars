def update_light(current: str) -> str:
    # Your code here.
    return "yellow" if current == "green" else "red" if current == "yellow" else "green"