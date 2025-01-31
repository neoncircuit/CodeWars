# Mumbling

## Instructions

This time no story, no theory. The examples below show you how to write function `accum`:

## Examples:

```
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
```

The parameter of accum is a string which includes only letters from `a..z` and `A..Z`.

## Given Code
```python
def accum(st):
    pass
```

## My Solution
```python
def accum(st):
    return "-".join(char.upper() + char().lower()*i for i, char in enumerate(st))
```
