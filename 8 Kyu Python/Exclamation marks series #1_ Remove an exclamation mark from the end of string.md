# Exclamation marks series #1: Remove an exclamation mark from the end of string

## Instructions

## Description:

Remove an exclamation mark from the end of a string. For a beginner kata, you can assume that the input data is always a string, no need to verify it.

## Examples

```
"Hi!"     ---> "Hi"
"Hi!!!"   ---> "Hi!!"
"!Hi"     ---> "!Hi"
"!Hi!"    ---> "!Hi"
"Hi! Hi!" ---> "Hi! Hi"
"Hi"      ---> "Hi"
```

## Given Code
```python
def remove(s):
    pass
```

## My Solution
```python
def remove(s):
    return s[0:-1] if s.endswith("!") else s
```
