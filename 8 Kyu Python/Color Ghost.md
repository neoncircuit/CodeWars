# Color Ghost

## Instructions

Create a class Ghost

Ghost objects are instantiated without any arguments.

Ghost objects are given a random color attribute of "white" or "yellow" or "purple" or "red" when instantiated

```
ghost = Ghost()
ghost.color  #=> "white" or "yellow" or "purple" or "red"
```

## Given Code
```python
class Ghost(object):
    pass
```

## My Solution
```python
import random

class Ghost(object):
    def __init__(self):
        # Assign a random color to the ghost
        self.color = random.choice(["white", "yellow", "purple", "red"])
```
