import urllib.parse

def generate_link(user):
    baseurl = "http://www.codewars.com/users/"
    username = urllib.parse.quote(user)
    return f"{baseurl}{username}"
