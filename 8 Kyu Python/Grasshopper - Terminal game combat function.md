# Grasshopper - Terminal game combat function

Create a combat function that takes the player's current health and the amount of damage recieved, and returns the player's new health. Health can't be less than 0.

# Given Code

```{python}
def combat(health, damage):
    #your code here
```

# My Solution

```{python}
def combat(health, damage):
    #your code here
    while health >= 0:
        if health < damage:
            return 0
        else: 
            return health - damage  
```
