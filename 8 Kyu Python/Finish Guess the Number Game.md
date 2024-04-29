# Finish Guess the Number Game

Imagine you are creating a game where the user has to guess the correct number. But there is a limit of how many guesses the user can do.

- If the user tries to guess more than the limit, the function should throw an error.
- If the user guess is right it should return true.
- If the user guess is wrong it should return false and lose a life.

Can you finish the game so all the rules are met?

# Given Code

```{python}
class Guesser:
    def __init__(self, number, lives):
        self.number = number
        self.lives = lives
  
    def guess(self,n):
        return False
```

# My Solution

```{python}
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
```
