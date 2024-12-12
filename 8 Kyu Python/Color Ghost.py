import random

class Ghost(object):
    def __init__(self):
        # Assign a random color to the ghost
        self.color = random.choice(["white", "yellow", "purple", "red"])