# Find numbers which are divisible by given number

Complete the function which takes two arguments and returns all numbers which are divisible by the given divisor. First argument is an array of numbers and the second is the divisor.

## Example(Input1, Input2 --> Output)

```
[1, 2, 3, 4, 5, 6], 2 --> [2, 4, 6]
```

# Given Code

```{typescript}
export function divisibleBy(numbers: number[], divisor: number): number[]{
  return []
}
```

# My Solution

```{typescript}
export function divisibleBy(numbers: number[], divisor: number): number[]{
  return numbers.filter((num) => num % divisor === 0);
}
```
