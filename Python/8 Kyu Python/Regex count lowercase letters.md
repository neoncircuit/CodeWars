# Regex count lowercase letters

Your task is simply to count the total number of lowercase letters in a string.

## Examples

"abc" ===> 3

"abcABC123" ===> 3

"abcABC123!@€£#$%^&*()_-+=}{[]|\':;?/>.<,~" ===> 3

"" ===> 0;

"ABC123!@€£#$%^&*()_-+=}{[]|\':;?/>.<,~" ===> 0

"abcdefghijklmnopqrstuvwxyz" ===> 26

# Given Code

```{python}
def lowercase_count(strng):
    # Your code here
```

# My Solution

```{python}
def lowercase_count(strng):
    # Your code here
    x = 0
    for i in strng:
        if(i.islower()):
            x += 1
    return x
```
