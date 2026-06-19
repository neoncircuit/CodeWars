# Basic Math (Add or Subtract)

## Instructions

In this kata, you will do addition and subtraction on a given string. The return value must be also a string.

Note: the input will not be empty.

## Examples
```
"1plus2plus3plus4"  --> "10"
"1plus2plus3minus4" -->  "2"
```

## Given Code
```
function calculate(str) {
  //your code here...
  return str;
}
```

## My Solution
```
function calculate(str) {
  //your code here...
  let result = str.replaceAll("plus", "+").replaceAll("minus", "-");
  if (result.endsWith("+") || result.endsWith("-")) {
    result = result.slice(0, -1);
  }
  return eval(result).toString();
}
```