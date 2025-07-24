# Invert values

Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.

```
[1, 2, 3, 4, 5] --> [-1, -2, -3, -4, -5]
[1, -2, 3, -4, 5] --> [-1, 2, -3, 4, -5]
[] --> []
```

# Given Code

```{typescript}
export function invert(array: number[]): number[] {
   return [];
}
```

# My Solution

```{typescript}
export function invert(array: number[]): number[] {
  const inverted = new Array<number>(array.length);
  for (let i = 0; i < array.length; i++) {
    inverted[i] = -array[i];
  }
  return inverted;
}
```
