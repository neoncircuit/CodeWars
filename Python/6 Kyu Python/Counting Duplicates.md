# Count the number of Duplicates
Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

## Example
```
"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
"indivisibility" -> 1 # 'i' occurs six times
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice
```

# Given Code

```{python}
def duplicate_count(text):
    # Your code goes here
```

# My Solution

```{python}
def duplicate_count(text):
    # Your code goes here
    
    # Empty Dictionary to store count of each character in input string
    charDict = {} 
    
    # Looping through each character in input string and converts it into lowercase
    for i in text.lower():
        
        # Check if char is alphanumeric
        if i.isalnum(): 
            
            # Checks if its already in charDict
            if i in charDict:
                charDict[i] += 1 # Increments its count by 1
            else:
                charDict[i] = 1 # Adds to charDict with a count of 1
    
    count = 0
    
    # Loops through the keys of charDict and counts number of keys that have a count greater than 1
    for j in charDict:
        if charDict[j] > 1:
            count += 1

    return count
```

# My Solution 2

```{python}
def duplicate_count(text):
    n = 0
    text = text.lower()
    for i in set(text):
        if text.count(i) > 1:
            n += 1
    return n
```
