# Sum Mixed Array

## Instructions

Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.

Return your answer as a number.

## Given Code
```
export function sumMix(x: any[]): number {

}
```

## My Solution
```
export function sumMix(x: any[]): number {
  let sum: number = 0;
  for (let i=0; i<x.length; i++) {
    sum += Number(x[i]);
  }
  return sum;
}
```