# Invert values

Instructions

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
