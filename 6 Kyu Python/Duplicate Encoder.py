def duplicate_encode(word):
    #your code here
    word = word.lower()
    wordDict = {}
    res = ""
    for i in word:
        if i in wordDict:
            wordDict[i] += 1
        else:
            wordDict[i] = 1
    
    for j in word:
        if wordDict[j] == 1:
            res += "("
        else:
            res += ")"
    return res
