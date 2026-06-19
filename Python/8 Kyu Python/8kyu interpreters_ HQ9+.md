# 8kyu interpreters: HQ9+

## Instructions

You task is to implement an simple interpreter for the notorious esoteric language HQ9+ that will work for a single character input:

- If the input is 'H', return 'Hello World!'
- If the input is 'Q', return the input
- If the input is '9', return the full lyrics of 99 Bottles of Beer. It should be formatted like this:

```
99 bottles of beer on the wall, 99 bottles of beer.
Take one down and pass it around, 98 bottles of beer on the wall.
98 bottles of beer on the wall, 98 bottles of beer.
Take one down and pass it around, 97 bottles of beer on the wall.
97 bottles of beer on the wall, 97 bottles of beer.
Take one down and pass it around, 96 bottles of beer on the wall.
...
...
...
2 bottles of beer on the wall, 2 bottles of beer.
Take one down and pass it around, 1 bottle of beer on the wall.
1 bottle of beer on the wall, 1 bottle of beer.
Take one down and pass it around, no more bottles of beer on the wall.
No more bottles of beer on the wall, no more bottles of beer.
Go to the store and buy some more, 99 bottles of beer on the wall.
```

- For everything else, don't return anything (return null in C#, None in Rust, and "" in Haskell).
(+ has no visible effects so we can safely ignore it.)

## Given Code
```python
def HQ9(code):
    pass
```

## My Solution
```python
def HQ9(code):
    match code:
        case "H":
            return "Hello World!"
        case "Q":
            return code
        case "9":
            return "\n".join(beer_song())

def beer_song():
    verses = []
    for i in range(99, 0, -1):
        if i > 1:
            verses.append(f"{i} bottles of beer on the wall, {i} bottles of beer.")
            verses.append(f"Take one down and pass it around, {i - 1} {'bottle' if i - 1 == 1 else 'bottles'} of beer on the wall.")
        else:
            verses.append(f"1 bottle of beer on the wall, 1 bottle of beer.")
            verses.append("Take one down and pass it around, no more bottles of beer on the wall.")
    verses.append("No more bottles of beer on the wall, no more bottles of beer.")
    verses.append("Go to the store and buy some more, 99 bottles of beer on the wall.")
    return verses

```
