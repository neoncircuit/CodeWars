# Parse float

## Instructions

Write function `parseFloat` which takes an input and returns a number or `Nothing` if conversion is not possible.

## Given Code
```
export function parseF(s:string): number|null {
  return null;
}
```

## My Solution
```
export function parseF(s: string): number | null {
  const parsedValue = parseFloat(s);
  return Number.isNaN(parsedValue) ? null : parsedValue;
}
```