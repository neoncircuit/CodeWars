def abbrev_name(name):
    nameOut = name.split(" ")
    i1 = nameOut[0][0].upper()
    i2 = nameOut[1][0].upper()
    initials = i1 + "." + i2
    return initials
