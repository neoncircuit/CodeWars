# Vowel remover

Create a function called shortcut to remove the lowercase vowels (a, e, i, o, u ) in a given string.

## Examples

"hello"     -->  "hll"
"codewars"  -->  "cdwrs"
"goodbye"   -->  "gdby"
"HELLO"     -->  "HELLO"

don't worry about uppercase vowels

y is not considered a vowel for this kata

# Given Code

```{python}
def shortcut( s ):
    # ...
```

# My Solution

```{python}
def shortcut( s ):
    vowels = "aeiou"
    
    for vowel in vowels:
        s = s.replace(vowel, "")
    
    return s
```
