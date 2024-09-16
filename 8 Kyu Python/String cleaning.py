def string_clean(s):
    """
    Function will return the cleaned string
    """
    # Your code here
    res = "".join(filter(lambda x: not x.isdigit(), s))
    
    return str(res)
