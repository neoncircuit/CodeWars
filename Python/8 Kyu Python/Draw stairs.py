def draw_stairs(n):
    x = ""
    for i in range(0, n):
        x += " " * i + "I\n"
    return x[:-1] # Remove the trailing newline character from the last row
