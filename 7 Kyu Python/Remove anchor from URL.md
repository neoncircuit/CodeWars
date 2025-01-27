# Remove anchor from URL

## Instructions

Complete the function/method so that it returns the url with anything after the anchor (`#`) removed.

## Examples

```
"www.codewars.com#about" --> "www.codewars.com"
"www.codewars.com?page=1" -->"www.codewars.com?page=1"
```

## Given Code
```python
def remove_url_anchor(url):
    # TODO: complete
```

## My Solution
```python
def remove_url_anchor(url):
    # TODO: complete
    return url.split("#", 1)[0]
```
