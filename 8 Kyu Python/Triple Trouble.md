# Triple Trouble

## Instructions

Create a function that will return a string that combines all of the letters of the three inputed strings in groups. Taking the first letter of all of the inputs and grouping them next to each other. Do this for every letter, see example below!

**E.g. Input: "aa", "bb" , "cc" => Output: "abcabc"**

Note: You can expect all of the inputs to be the same length.



## Given Code
```python
def triple_trouble(one, two, three):
    #your code here
```

## My Solution
```python
def triple_trouble(one, two, three):
    #your code here
    return "".join(a+b+c for a,b,c in zip(one,two,three))
```
