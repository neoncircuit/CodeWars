# Simple beads count

## Instructions

Two red beads are placed between every two blue beads. There are N blue beads. After looking at the arrangement below work out the number of red beads.

<span style="color: blue;">@</span> <span style="color: red;">@@</span> <span style="color: blue;">@</span> <span style="color: red;">@@</span> <span style="color: blue;">@</span> <span style="color: red;">@@</span> <span style="color: blue;">@</span> <span style="color: red;">@@</span> <span style="color: blue;">@</span> <span style="color: red;">@@</span> <span style="color: blue;">@</span>

Implement a function returning the number of <span style="color: red;">red</span> beads.
If there are less than 2 blue beads return 0.

## Given Code
```
export function countRedBeads(n: number): number {
  return 0; //your code here
}
```

## My Solution
```
export function countRedBeads(n: number): number {
  //your code here
  if (n < 2) {
    return 0;
  }
  let result = (n - 1) * 2;
  return result;
}
```
