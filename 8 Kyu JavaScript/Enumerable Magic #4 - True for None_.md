# Enumerable Magic #4 - True for None?

## Instructions

Write a function that takes two arguments: an array and a callback function (in Ruby: a block).

The function should return `true` if the callback / block returns `false` for all of the items in the array, or if the array is empty; otherwise return `false`.

## Given Code
```
function none(arr, fun){
  // ...
}
```

## My Solution
```
function none(arr, fun){
  // ...
  return arr.length === 0 || arr.every(item => !fun(item));
}
```