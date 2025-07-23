# Sum Mixed Array

**Difficulty:** 8 Kyu  
**Language:** TypeScript  
**Date:** 2025-07-23

## Problem Description

Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.

Return your answer as a number.

## Provided/Starter Code

```typescript
export function sumMix(x: any[]): number {

}
```

## My Solution

```typescript
export function sumMix(x: any[]): number {
  let sum: number = 0;
  for (let i=0; i<x.length; i++) {
    sum += Number(x[i]);
  }
  return sum;
}
```

*Uploaded on 2025-07-23 15:11:35 using CodeWars GUI*