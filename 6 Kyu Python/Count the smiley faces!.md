# Count the smiley faces!

Given an array (arr) as an argument complete the function ```countSmileys``` that should return the total number of smiling faces.

Rules for a smiling face:

Each smiley face must contain a valid pair of eyes. Eyes can be marked as ```:``` or ```;```
A smiley face can have a nose but it does not have to. Valid characters for a nose are ```-``` or ```~```
Every smiling face must have a smiling mouth that should be marked with either ```)``` or ```D```
No additional characters are allowed except for those mentioned.

Valid smiley face examples: ```:) :D ;-D :~)```

Invalid smiley faces: ```;( :> :} :]```

## Example
```
countSmileys([':)', ';(', ';}', ':-D']);       // should return 2;
countSmileys([';D', ':-(', ':-)', ';~)']);     // should return 3;
countSmileys([';]', ':[', ';*', ':$', ';-D']); // should return 1;
```

## Note
In case of an empty array return 0. You will not be tested with invalid input (input will always be an array). Order of the face (eyes, nose, mouth) elements will always be the same.

# Given Code

```{python}
def count_smileys(arr):
    return #the number of valid smiley faces in array/list
```

# My Solution

```{python}
import re

def count_smileys(arr):
    # the number of valid smiley faces in array/list
    regex = r"[:;][-~]?[)D]"
    matchingStrings = re.findall(regex, ' '.join(arr))
    return len(matchingStrings)
```

# My Solution 2
```
def count_smileys(arr):
    eyes = [":", ";"]
    noses = ["", "-", "~"]
    mouths = [")", "D"]
    count = 0
    for eye in eyes:
        for nose in noses:
            for mouth in mouths:
                face = eye + nose + mouth
                count += arr.count(face)
    return count
```

# My Solution 3
```
def count_smileys(arr):
    total = 0
    eyes = ':;'
    nose = '-~'
    mouth = ')D'
    for char in arr:

        if len(char) == 3:
            if char[0] in eyes and char[1] in nose and char[2] in mouth:
                total += 1

        elif len(char) == 2:
            if char[0] in eyes and char[1] in mouth:
                total += 1
    return total
```
