import re

def validate_usr(username):
    #your code here
    return bool(re.fullmatch(r"[a-z0-9_]{4,16}", username))
