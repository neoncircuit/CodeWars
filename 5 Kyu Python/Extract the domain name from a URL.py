def domain_name(url):
    # Remove the protocol (http:// or https://)
    url = url.replace("http://", "").replace("https://", "")
    
    # Remove "www." if present
    url = url.replace("www.", "")
    
    # Split by "." and take the first part
    return url.split(".")[0]