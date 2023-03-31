def number(lines):
    #your code here
    noOfLines = []
    lineNo = 1
    for i in lines:
        noOfLines.append(str(lineNo) + ": " + i)
        lineNo += 1
    return noOfLines
