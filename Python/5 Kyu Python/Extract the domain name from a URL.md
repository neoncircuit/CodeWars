# Extract the domain name from a URL

## Instructions

Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

```
* url = "http://github.com/carbonfive/raygun" -> domain name = "github"
* url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
* url = "https://www.cnet.com"                -> domain name = cnet"
```

## Given Code
```python
def domain_name(url):
    pass
```

## My Solution
```python
def domain_name(url):
    # Remove the protocol (http:// or https://)
    url = url.replace("http://", "").replace("https://", "")
    
    # Remove "www." if present
    url = url.replace("www.", "")
    
    # Split by "." and take the first part
    return url.split(".")[0]
```
