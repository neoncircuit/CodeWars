# Identify Case

We’ve all seen katas that ask for conversion from snake-case to camel-case, from camel-case to snake-case, or from camel-case to kebab-case — the possibilities are endless.

But if we don’t know the case our inputs are in, these are not very helpful.

## Task:
So the task here is to implement a function that takes a string and returns a string with the case the input is in. The possible case types are `"kebab"`, `"camel"`, and `"snake"`. If none of the cases match with the input, or if there are no separators / case changes in the input, return `"none"`. Inputs will only have letters (no numbers or special characters).

## Some definitions

- Kebab case: `lowercase-words-separated-by-hyphens`

- Camel case: `lowercaseFirstWordFollowedByCapitalizedWords`

- Snake case: `lowercase_words_separated_by_underscores`

## Examples:
```
"hello-world" => "kebab"
"hello-to-the-world" => "kebab"
"helloWorld" => "camel"
"helloToTheWorld" => "camel"
"hello_world" => "snake"
"hello_to_the_world" => "snake"
"hello__world" => "none"
"hello_World" => "none"
"helloworld" => "none"
"hello-World" => "none"
```

# Given Code

```python
def case_id(c_str):
    # your code here
```

# My Solution

```python
def case_id(c_str: str) -> str:
    # your code here
    if "-" in c_str:
        if "_" in c_str or "--" in c_str or any(c.isupper() for c in c_str): 
            return "none" 
        return "kebab"
        
    if "_" in c_str:
        if "-" in c_str or "__" in c_str or any(c.isupper() for c in c_str):
            return "none" 
        return "snake" 
        
    if "-" not in c_str and "_" not in c_str:
        if c_str.lower() == c_str:
            return "none"
        if not c_str[0].islower():
            return "none"
        if any(c == "_" or c == "-" for c in c_str):
            return "none"
        return "camel"
    
    return "none"
```

# Complexity Analysis

**Time Complexity:** O(n)

**Space Complexity:** O(1)

**Explanation:**
**Time: O(n)** - Linear time complexity. The code iterates through the input once (using loops like for, while, forEach, map, filter, reduce). The number of operations grows proportionally with the input size.

**Space: O(1)** - Constant space complexity. The code uses a fixed amount of memory regardless of input size.
