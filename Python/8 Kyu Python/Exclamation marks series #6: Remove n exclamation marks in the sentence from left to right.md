# Exclamation marks series 6: Remove n exclamation marks in the sentence from left to right

## Description:
Remove n exclamation marks in the sentence from left to right. n is positive integer.

## Examples
```{python}
remove("Hi!",1) === "Hi"
remove("Hi!",100) === "Hi"
remove("Hi!!!",1) === "Hi!!"
remove("Hi!!!",100) === "Hi"
remove("!Hi",1) === "Hi"
remove("!Hi!",1) === "Hi!"
remove("!Hi!",100) === "Hi"
remove("!!!Hi !!hi!!! !hi",1) === "!!Hi !!hi!!! !hi"
remove("!!!Hi !!hi!!! !hi",3) === "Hi !!hi!!! !hi"
remove("!!!Hi !!hi!!! !hi",5) === "Hi hi!!! !hi"
remove("!!!Hi !!hi!!! !hi",100) === "Hi hi hi"
```

# Given Code

```{python}
def remove(st, n):
    pass
```

# My Solution

```{python}
def remove(st, n):
    count = 0
    result = ''
    for char in st:
        if char == '!' and count < n:
            count += 1
        else:
            result += char
    return result
```
