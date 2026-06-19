def filter_list(l):
    #'return a new list with the strings filtered out'
    final = []
    for i in l:
        if type(i) == int:
            final.append(i)
    return final
