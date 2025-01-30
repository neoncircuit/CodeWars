def capitals(word):
    #your code here
    res = [idx for idx in range(len(word)) if word[idx].isupper()]
    return res