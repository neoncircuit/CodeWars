# Abbreviate a Two Word Name 

Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot separating them.

It should look like this:

```Sam Harris``` => ```S.H```

```patrick feeney``` => ```P.F```

# Given Code

```{python}
def abbrev_name(name):
    return
```

# My Solution

```{python}
def abbrev_name(name):
    nameOut = name.split(" ")
    i1 = nameOut[0][0].upper()
    i2 = nameOut[1][0].upper()
    initials = i1 + "." + i2
    return initials
```
