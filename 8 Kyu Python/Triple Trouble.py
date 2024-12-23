def triple_trouble(one, two, three):
    #your code here
    return "".join(a+b+c for a,b,c in zip(one,two,three))