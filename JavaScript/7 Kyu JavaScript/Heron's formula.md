# Heron's formula

## Instructions

Write function heron which calculates the area of a triangle with sides a, b, and c.

Heron's formula:

$
\sqrt{s*(s - a)*(s - b)*(s - c)} \quad 
$
\
$
\text{where: } s = \frac{a + b + c}{2}
$

## Notes

- All inputs are valid triangles with integer sides.

- You do not need to round anything. Answers will be tested for correctness within a margin of 0.01.

## Given Code
```
function heron(a, b, c) {
  return 0;
}
```

## My Solution
```
function heron(a, b, c) {
  let s = (a+b+c)/2;
  let formula = s*(s-a)*(s-b)*(s-c);
  return Math.sqrt(formula);
}
```