import re

def count_smileys(arr):
    # the number of valid smiley faces in array/list
    regex = r"[:;][-~]?[)D]"
    matchingStrings = re.findall(regex, ' '.join(arr))
    return len(matchingStrings)
