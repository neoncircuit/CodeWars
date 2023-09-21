def add_length(str_):
    #your code here
    x = str_.split()
    y = []
    for i in x:
        y.append(i + ' ' + str(len(i)))
    return y
