# Draw stairs

Given a number n, draw stairs using the letter "I", n tall and n wide, with the tallest in the top left.

## For example n = 3 result in:
"I\n I\n  I"

## or printed:
I
 I
  I

## Another example, a 7-step stairs should be drawn like this:
I
 I
  I
   I
    I
     I
      I
  
# Given Code

```{python}
def draw_stairs(n):
    pass
```

# My Solution

```{python}
def draw_stairs(n):
    x = ""
    for i in range(0, n):
        x += " " * i + "I\n"
    return x[:-1] # Remove the trailing newline character from the last row
```
