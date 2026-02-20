def testit(s: str) -> str:
    # Your code here
    words = s.split(" ")
    res = []
    
    for word in words:
        if len(word) == 0:
            res.append("")
        elif len(word) == 1:
            res.append(word.upper())
        else:
            res.append(word[:-1] + word[-1].upper())
            
    return " ".join(res)