# Translate anything into French !

Sacrebleu!

French can be pretty hard to master, and it might take you quite a while if you want to learn it from scratch...

Fortunately, we come to the rescue with this kata, and you will soon be able to translate anything into French.

French often use the words "Baguette" (in reference to their marvelous bread: https://en.wikipedia.org/wiki/Baguette). Moreover, they like to shout "Encore, encore!" at the end of an accordeon concert. Here we will shout "Encore!" at the end of our sentence.

In this kata, our i_speak_french method will translate any sentence argument into its French translation :

- Every word from the sentence must be translated into "Baguette" (if it is the begining of the sentence), or "baguette" otherwise.

- Every sentence must end by an "Encore!" exclamation. A sentence is ended by a final dot ("."), or by the end of the string argument.

You will expect a string as argument, no non-alphabetical values will be used.

# Given Code

```python
def i_speak_french(sentence):
    # Parlez-vous français ? :)
    pass
```

# My Solution

```python
import re

def i_speak_french(speech: str) -> str:
    # Parlez-vous français ? :)
    sentences = re.split(r'[.!?]+', speech)
    sentences = [s.strip() for s in sentences if s.strip()]
    
    translated_sentences = []
    for sentence in sentences:
        words = sentence.split()
        count = len(words)
        if count == 0:
            continue
        
        baguette_words = ["baguette"] * count
        baguette_words[0] = "Baguette"
        
        translated_sentence = " ".join(baguette_words) + " Encore!"
        translated_sentences.append(translated_sentence)
    
    return " ".join(translated_sentences)
```

# Complexity Analysis

**Time Complexity:** O(n)

**Space Complexity:** O(n)

**Explanation:**
**Time: O(n)** - Linear time complexity. The code iterates through the input once (using loops like for, while, forEach, map, filter, reduce). The number of operations grows proportionally with the input size.

**Space: O(n)** - Linear space complexity. Data structures (arrays, objects, sets, maps) were detected that may grow proportionally with input size.
