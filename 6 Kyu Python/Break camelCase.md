# Break camelCase

Complete the solution so that the function will break up camel casing, using a space between words.

## Example
```
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""
```

# Given Code

```{python}
def solution(s):
    pass
```

# My Solution

```{python}
def solution(s):
    # Checking if s is empty
    if s == "":
        return ""
    
    # Empty output string
    s2 = ""
    
    # Loop through each character in the input string s
    for i in range(0, len(s)):
        # Check if the current character is uppercase
        if s[i].isupper():
            # Add a space to the output string s2
            s2 += " "
        
        # Add the current character to the output string s2
        s2 += s[i]
            
    return s2
```
