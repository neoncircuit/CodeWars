# Grasshopper - Terminal game move function

## Instructions

## Terminal game move function

In this game, the hero moves from left to right. The player rolls the dice and moves the number of spaces indicated by the dice **two times**.

Create a function for the terminal game that takes the current position of the hero and the roll (1-6) and return the new position.

## Example:

```
move(3, 6) should equal 15
```

## Given Code
```python
def move(position, roll):
    # your code here
```

## My Solution
```python
def move(position:int, roll:int) -> int:
    # your code here
    return position + (roll * 2)
```
