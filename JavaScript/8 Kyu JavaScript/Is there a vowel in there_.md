# Is there a vowel in there?

## Instructions

Given an array of numbers, check if any of the numbers are the character codes for lower case vowels `(a, e, i, o, u)`.

If they are, change the array value to a string of that vowel.

input `[100,100,116,105,117,121]=>[100,100,116,"i","u",121]` output Return the resulting array.

## Given Code
```
function isVow(a){
  return a // your code here
}
```

## My Solution
```
function isVow(a){
  const vowels = {
    97: 'a',
    101: 'e',
    105: 'i',
    111: 'o',
    117: 'u'
  };
  const result = [];
  for (let i = 0; i < a.length; i++) {
    const num = a[i];
    if (vowels.hasOwnProperty(num)) {
      result.push(vowels[num]);
    } else {
      result.push(num);
    }
  }
  return result;
}
```