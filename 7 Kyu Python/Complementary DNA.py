def DNA_strand(dna):
    # code here
    dnaResult = ""
    for i in dna:
        match i:
            case "A":
                dnaResult += "T"
            case "T":
                dnaResult += "A" 
            case "C":
                dnaResult += "G"
            case "G":
                dnaResult += "C" 
    return dnaResult
