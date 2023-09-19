# Double Char

Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

## Examples (Input -> Output):
* "String"      -> "SSttrriinngg"
* "Hello World" -> "HHeelllloo  WWoorrlldd"
* "1234!_ "     -> "11223344!!__  "

# Given Code

```{python}
def double_char(s):
    pass
```

# My Solution

```{python}
def double_char(s):
    newstring = ""
    for i in s:
        newstring += i*2
    return newstring
```
