def fake_bin(x):
    res = ""
    for i in x:
        if i >= '5':
            res += '1'
        else:
            res += '0'
    return res
