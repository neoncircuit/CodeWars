# Convert a String to a Number!

## Instructions

Note: This kata is inspired by Convert a Number to a String!. Try that one too.

We need a function that can transform a string into a number. What ways of achieving this do you know?

Note: Don't worry, all inputs will be strings, and every string is a perfectly valid representation of an integral number.

## Examples
```
"1234" --> 1234
"605"  --> 605
"1405" --> 1405
"-7" --> -7
```

## Given Code
```
const stringToNumber = function(str){
  // put your code here
  return null;
}
```

## My Solution
```
const stringToNumber = function(str){
  // put your code here
  return parseInt(str);
}
```