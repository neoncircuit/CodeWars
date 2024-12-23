# Neutralisation

## Instructions

Given two strings comprised of `+` and `-`, return a new string which shows how the two strings interact in the following way:

- When positives and positives interact, they remain positive.

- When negatives and negatives interact, they remain negative.

- But when negatives and positives interact, they become neutral, and are shown as the number 0.

## Worked Example
```
("+-+", "+--") ➞ "+-0"
# Compare the first characters of each string, then the next in turn.
# "+" against a "+" returns another "+".
# "-" against a "-" returns another "-".
# "+" against a "-" returns "0".
# Return the string of characters.
```

## Examples
```
("--++--", "++--++") ➞ "000000"

("-+-+-+", "-+-+-+") ➞ "-+-+-+"

("-++-", "-+-+") ➞ "-+00"
```

## Notes

The two strings will be the same length.

## Given Code
```python
def neutralise(s1, s2):
    pass
```

## My Solution
```python
def neutralise(s1, s2):
    result = []
    for char1, char2 in zip(s1, s2):
        if char1 == char2:
            result.append(char1)
        else:
            result.append("0")
    return "".join(result)
```
