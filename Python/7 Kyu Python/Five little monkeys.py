def monkeys():
    # return the complete lyrics
    w="Five Four Three Two One".split()
    a=" little monkey%s jumping on the bed,"
    b=" fell off and bumped his head."
    c="Mother called the doctor and the doctor said:"
    r=[]
    for i in range(5):
        r+=["%s%s"%(w[i],a%("s"*(i<4))),["One","He"][i==4]+b,c,["No more monkeys jumping on the bed!","Put those monkeys right to bed!"][i==4],""]
    return"\n".join(r[:-1])