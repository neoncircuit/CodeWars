# Your order, please

Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.

## Examples
```
"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
""  -->  ""
```

# Given Code

```{python}
def order(sentence):
  # code here
  return
```

# My Solution

```{python}
def order(sentence):
  # Split the input string into a list of words
    words = sentence.split()
    
    # Create a dictionary to store the order of each word
    order = {}
    for word in words:
        for char in word:
            if char.isdigit():
                order[word] = int(char)
    
    # Sort the words based on their order
    sorted_words = sorted(words, key=lambda x: order[x])
    
    # Join the sorted words back into a string
    result = ' '.join(sorted_words)
    
    return result
```


# My Solution 2

```{python}
def order(sentence):
    if not sentence:
        return ""
    result = []    # The list that will eventually become our sentence
      
    split_up = sentence.split() # The original sentence turned into a list
  
    for i in range(1, 10):
        for item in split_up:
            if str(i) in item:
                 result.append(item)    # Adds them in numerical order since it cycles through i first
  
    return " ".join(result)
```
