# Basic Calculator

Write a function called that takes 3 values. The first and third values are numbers. The second value is a character.

- If the character is "+" , "-", "*", or "/", the function will return the result of the corresponding mathematical function on the two numbers.
- If the string is not one of the specified characters, the function should return null (throw an `ArgumentException` in C#).
- Keep in mind, you cannot divide by zero. If an attempt to divide by zero is made, return `null` / `None` (Python) / throw an `ArgumentException` (C#).

```
(2,"+", 4) --> 6
(6,"-", 1.5) --> 4.5
(-4,"*", 8) --> -32
(49,"/", -7) --> -7
(8,"m", 2) --> null
(4,"/",0) --> null
```

# Given Code

```python
def calculate(num1, operation, num2): 
    # your code here
    pass
```

# My Solution

```python
import operator

def calculate(num1: float | int, operation: str, num2: float | int) -> str: 
    # your code here
    OPERATORS = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }
    func = OPERATORS.get(operation)
    
    if func is None:
        return None
    
    if operation == '/' and num2 == 0:
        return None

    try:
        return func(num1, num2)
    except ZeroDivisonError:
        return None
```

# Complexity Analysis

**Time Complexity:** O(1)

**Space Complexity:** O(1)

**Explanation:**
**Time: O(1)** - Constant time complexity. The code performs a fixed number of operations regardless of input size. No loops or recursive calls that depend on input size were detected.

**Space: O(1)** - Constant space complexity. The code uses a fixed amount of memory regardless of input size.
