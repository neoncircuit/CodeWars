# Mythical Heads and Tails

## Instructions

You're in ancient Greece and giving Philoctetes a hand in preparing a training exercise for Hercules! You've filled a pit with two different ferocious mythical creatures for Hercules to battle!

The formidable **"Orthus"** is a 2 headed dog with 1 tail. The mighty **"Hydra"** has 5 heads and 1 tail.

Before Hercules goes in, he asks you "How many of each beast am I up against!?".

You know the total number of heads and the total number of tails, that's the dangerous parts, right? But you didn't consider how many of each beast.

## Task

Given the number of heads and the number of tails, work out the number of each mythical beast!

The data is given as two parameters. Your answer should be returned as an array:

```
 VALID ->      [24 , 15]           INVALID ->  "No solutions"
```

If there aren't any cases for the given amount of heads and tails - return "No solutions" or null (C#).

## Given Code
```python
def beasts(heads, tails):
    pass # [orthus, hydra]
```

## My Solution
```python
def beasts(heads, tails):
    # [orthus, hydra]
    # heads = 2o + 5h
    # tails = o + h
    if (heads - 2 * tails) % 3 != 0 or (heads - 2 * tails) < 0:
        return "No solutions"
    
    H = (heads - 2 * tails) // 3
    O = tails - H
    
    if O < 0 or H < 0:
        return "No solutions"
    
    return [O, H]
```
