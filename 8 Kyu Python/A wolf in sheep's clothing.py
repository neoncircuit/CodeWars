def warn_the_sheep(queue):
    if queue[-1] == "wolf":
        return "Pls go away and stop eating my sheep"
    else:
        sheep_number = len(queue) - queue.index("wolf") - 1
        return f"Oi! Sheep number {sheep_number}! You are about to be eaten by a wolf!"
