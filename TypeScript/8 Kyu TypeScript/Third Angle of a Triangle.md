# Third Angle of a Triangle

## Instructions

You are given two interior angles (in degrees) of a triangle.

Write a function to return the 3rd.

Note: only positive integers will be tested.

https://en.wikipedia.org/wiki/Triangle

## Given Code
```
export const otherAngle = (a: number, b: number): number => {
  return 0;
}
```

## My Solution
```
export const otherAngle = (a: number, b: number): number => {
  return 180 - a - b;
}
```