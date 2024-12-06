# Grader

## Instructions

Create a function that takes a number as an argument and returns a grade based on that number.


| Score                            | Grade  |
| :------------------------------- | :-----: |
| Anything greater than 1 or less than 0.6 | "F"    |
| 0.9 or greater                  | "A"     |
| 0.8 or greater                  | "B"     |
| 0.7 or greater                  | "C"     |
| 0.6 or greater                  | "D"     |

Examples:

```
grader(0)   should be "F"
grader(1.1) should be "F"
grader(0.9) should be "A"
grader(0.8) should be "B"
grader(0.7) should be "C"
grader(0.6) should be "D"
```

## Given Code
```python
def grader(score):
    return 'F'
```

## My Solution
```python
def grader(score):
    match score:
        case s if 0.9 <= s <= 1:
            return "A"            
        case s if 0.8 <= s < 0.9:
            return "B"            
        case s if 0.7 <= s < 0.8:
            return "C"            
        case s if 0.6 <= s < 0.7:
            return "D"            
        case _:
            return "F"
```
