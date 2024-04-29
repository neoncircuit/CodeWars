class NoLivesLeftException(Exception):
    # Custom exception to indicate no lives are left for guessing.
    pass

class Guesser:
    def __init__(self, number, lives):
        self.number = number
        self.lives = lives
  
    def guess(self, n):
        while self.lives > 0:
            if n == self.number:
                return True
            else:
                self.lives -= 1
                return False
            break
        # Throw a custom exception when no lives are left
        raise NoLivesLeftException("Omae wa mo shindeiru")
