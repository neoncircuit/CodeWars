# Exclamation marks series #4: Remove all exclamation marks from sentence but ensure a exclamation mark at the end of string

## Instructions

## Description:

Remove all exclamation marks from sentence but ensure a exclamation mark at the end of string. For a beginner kata, you can assume that the input data is always a non empty string, no need to verify it.

## Examples

```
"Hi!"     ---> "Hi!"
"Hi!!!"   ---> "Hi!"
"!Hi"     ---> "Hi!"
"!Hi!"    ---> "Hi!"
"Hi! Hi!" ---> "Hi Hi!"
"Hi"      ---> "Hi!"
```

## Given Code
```python
def remove(st):
    pass
```

## My Solution
```python
def remove(st):
    return st.replace("!", "") + "!"
```
