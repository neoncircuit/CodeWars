# Is it a palindrome?

## Instructions

Write a function that checks if a given string (case insensitive) is a palindrome.

A palindrome is a word, number, phrase, or other sequence of symbols that reads the same backwards as forwards, such as `madam` or `racecar`.

## Given Code
```
export function isPalindrome(x: string): boolean {
  return true
}
```

## My Solution
```
export function isPalindrome(x: string): boolean {
  const lower = x.toLowerCase();
  const reversed = lower.split('').reverse().join('');
  return lower === reversed ? true : false;
}
```