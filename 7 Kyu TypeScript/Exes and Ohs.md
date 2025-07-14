# Exes and Ohs

## Instructions

Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

## Examples input/output:
```
XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false
```

## Given Code
```
export function xo(str: string) : boolean {
  // your code here
}
```

## My Solution
```
export function xo(str: string) : boolean {
  // your code here
  let countExes = 0;
  let countOhhs = 0;
  const lowercasedStr = str.toLowerCase();

  for (const char of lowercasedStr) {
    if (char === 'x') {
      countExes++;
    }
    if (char === 'o') {
      countOhhs++;
    }
  }
  return countExes === countOhhs;
}
```