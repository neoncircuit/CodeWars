# Testing 1-2-3

Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.

Write a function which takes a list of strings and returns each line prepended by the correct number.

The numbering starts at 1. The format is ```n: string```. Notice the colon and space in between.

## Examples: (Input --> Output)
```
[] --> []
["a", "b", "c"] --> ["1: a", "2: b", "3: c"]
```

# Given Code

```{python}
def number(lines):
    #your code here
```

# My Solution

```{python}
def number(lines):
    #your code here
    noOfLines = []
    lineNo = 1
    for i in lines:
        noOfLines.append(str(lineNo) + ": " + i)
        lineNo += 1
    return noOfLines
```
