# Exclamation marks series #2: Remove all exclamation marks from the end of sentence

## Instructions

## Description:

Remove all exclamation marks from the end of sentence.

## Examples

```
"Hi!"     ---> "Hi"
"Hi!!!"   ---> "Hi"
"!Hi"     ---> "!Hi"
"!Hi!"    ---> "!Hi"
"Hi! Hi!" ---> "Hi! Hi"
"Hi"      ---> "Hi"
```

## Given Code
```python
def remove(st):
    pass
```

## My Solution
```python
def remove(st):
    return st.rstrip("!")
```
