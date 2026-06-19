# Five little monkeys

Return the lyrics of the nursery rhyme "Five little monkeys" (see below).

But even monkeys can copy-paste, so you have to be smarter and make it short, because your code can be maximum 450 bytes long! (The original text is 800 bytes)

Hint: use loops and variables for repeated text, or any other way to reduce your code size.

When you solved this kata, try [N Little Animals](https://www.codewars.com/kata/696eb14a49272fa3ebe38aff/) too!

Happy coding!

```
Five little monkeys jumping on the bed,
One fell off and bumped his head.
Mother called the doctor and the doctor said:
No more monkeys jumping on the bed!

Four little monkeys jumping on the bed,
One fell off and bumped his head.
Mother called the doctor and the doctor said:
No more monkeys jumping on the bed!

Three little monkeys jumping on the bed,
One fell off and bumped his head.
Mother called the doctor and the doctor said:
No more monkeys jumping on the bed!

Two little monkeys jumping on the bed,
One fell off and bumped his head.
Mother called the doctor and the doctor said:
No more monkeys jumping on the bed!

One little monkey jumping on the bed,
He fell off and bumped his head.
Mother called the doctor and the doctor said:
Put those monkeys right to bed!
```

# Given Code

```python
def monkeys():
    # return the complete lyrics
    return "Five little monkeys..."
```

# My Solution

```python
def monkeys():
    # return the complete lyrics
    w="Five Four Three Two One".split()
    a=" little monkey%s jumping on the bed,"
    b=" fell off and bumped his head."
    c="Mother called the doctor and the doctor said:"
    r=[]
    for i in range(5):
        r+=["%s%s"%(w[i],a%("s"*(i<4))),["One","He"][i==4]+b,c,["No more monkeys jumping on the bed!","Put those monkeys right to bed!"][i==4],""]
    return"\n".join(r[:-1])
```

# Complexity Analysis

**Time Complexity:** O(n)

**Space Complexity:** O(n)

**Explanation:**
**Time: O(n)** - Linear time complexity. The code iterates through the input once (using loops like for, while, forEach, map, filter, reduce). The number of operations grows proportionally with the input size.

**Space: O(n)** - Linear space complexity. Data structures (arrays, objects, sets, maps) were detected that may grow proportionally with input size.
