# Build Tower

Build a pyramid-shaped tower, as an array/list of strings, given a positive integer ```number of floors```. A tower block is represented with ```"*"``` character.

For example, a tower with 3 floors looks like this:
```
[
  "  *  ",
  " *** ", 
  "*****"
]
```

And a tower with 6 floors looks like this:

```
[
  "     *     ", 
  "    ***    ", 
  "   *****   ", 
  "  *******  ", 
  " ********* ", 
  "***********"
]
```

# Given Code

```{python}
def tower_builder(n_floors):
    # build here
```

# My Solution

```{python}
def tower_builder(n_floors):
    # build here
    res = []
    width = n_floors*2 - 1
    for i in range(n_floors):
        numBlocks = i*2 + 1
        spaces = " " * ((width-numBlocks) // 2)
        blocks = "*" * numBlocks
        row = spaces + blocks + spaces
        res.append(row)
    return res
```
