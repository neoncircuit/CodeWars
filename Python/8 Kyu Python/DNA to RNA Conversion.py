def dna_to_rna(dna):
    dnaResult = ""
    for i in dna:
        match i:
            case "T":
                dnaResult += "U"
            case "G":
                dnaResult += "G"
            case "C":
                dnaResult += "C"
            case "A":
                dnaResult += "A"
    return dnaResult
