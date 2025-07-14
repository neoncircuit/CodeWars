# Grasshopper - Terminal game move function

## Instructions

In this game, the hero moves from left to right. The player rolls the die and moves the number of spaces indicated by the die **two times**.

Create a function for the terminal game that takes the current position of the hero and the roll (1-6) and return the new position.

## Example:
```
move(3, 6) should equal 15
```

## Given Code
```
export function move(pos: number, roll: number): number {
  // your code here
}
```

## My Solution
```
export function move(pos: number, roll: number): number {
  // your code here
  return pos + (roll * 2);
}
```