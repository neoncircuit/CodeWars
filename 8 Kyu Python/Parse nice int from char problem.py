def get_age(age):
    #your code here
    num = ""
    for c in age:
        if c.isdigit():
            num += c
    return int(num)
